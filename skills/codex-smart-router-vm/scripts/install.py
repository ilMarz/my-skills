#!/usr/bin/env python3
"""Installazione locale conservativa, Python 3.9+, nessuna dipendenza esterna."""
import argparse
import os
from pathlib import Path
import shutil
import sys
import uuid

NAME = 'codex-smart-router-vm'
START = b'<!-- codex-smart-router-vm:begin -->'
END = b'<!-- codex-smart-router-vm:end -->'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Applica il piano; default: sola anteprima')
    parser.add_argument('--home', type=Path, default=Path.home(), help='Home utente; utile per test isolati')
    parser.add_argument('--codex-home', type=Path, help='Home Codex esplicita; altrimenti CODEX_HOME o HOME/.codex')
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1]
    home = args.home.expanduser().resolve()
    codex_home = (args.codex_home or Path(os.environ.get('CODEX_HOME', str(home / '.codex')))).expanduser().resolve()
    dest = home / '.agents' / 'skills' / NAME
    guide = codex_home / 'AGENTS.md'
    override = codex_home / 'AGENTS.override.md'
    if override.exists() and override.read_bytes().strip():
        raise ValueError('AGENTS.override.md attivo: integra manualmente il frammento nel file effettivo; nessuna modifica applicata.')
    if guide.is_symlink() or dest.is_symlink():
        raise ValueError('Destinazione simbolica: usare installazione manuale dopo verifica; nessuna modifica.')
    legacy = codex_home / 'skills' / NAME
    if legacy.exists() or legacy.is_symlink():
        raise ValueError('Skill omonima nella home Codex: risolvere il duplicato manualmente; nessuna modifica.')
    old = guide.read_bytes() if guide.exists() else b''
    fragment = (source / 'templates' / 'AGENTS.fragment.md').read_bytes()
    if START in old or END in old:
        if old.count(START) != 1 or old.count(END) != 1 or fragment not in old:
            raise ValueError('Blocco router esistente diverso o incompleto: preservato, richiede confronto manuale.')
        new = old
    else:
        new = old + (b'\n\n' if old else b'') + fragment
    if len(new) > 32768:
        raise ValueError('AGENTS.md supererebbe 32 KiB: integrare manualmente considerando il limite di istruzioni.')
    if dest.exists():
        expected = {f.relative_to(source): f.read_bytes() for f in source.rglob('*') if f.is_file()}
        actual = {f.relative_to(dest): f.read_bytes() for f in dest.rglob('*') if f.is_file()}
        if actual != expected:
            raise ValueError('Skill esistente diversa: non viene sovrascritta. Confrontare e aggiornare manualmente.')
    print('Skill:', dest, '(già identica)' if dest.exists() else '(nuova)')
    print('Istruzioni:', guide, '(invariate)' if old == new else '(aggiunta in coda con backup)')
    print('config.toml e ruoli globali: nessuna modifica.')
    if not args.apply:
        print('ANTEPRIMA. Per installare ripetere con --apply.')
        return
    # Eseguire senza modifiche concorrenti a questi percorsi.
    created = False
    try:
        if not dest.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source, dest)
            created = True
        if old != new:
            codex_home.mkdir(parents=True, exist_ok=True)
            if guide.exists():
                with guide.open('r+b') as stream:
                    import fcntl
                    fcntl.flock(stream, fcntl.LOCK_EX)
                    if stream.read() != old:
                        raise ValueError('AGENTS.md cambiato durante installazione: interrotto.')
                    backup = guide.with_name('AGENTS.md.router-backup-' + uuid.uuid4().hex)
                    with backup.open('xb') as b:
                        b.write(old)
                    print('Backup:', backup)
                    stream.seek(0, 2)
                    stream.write(new[len(old):])
                    stream.flush()
                    os.fsync(stream.fileno())
            else:
                with guide.open('xb') as stream:
                    stream.write(new)
        print('Installazione completata nei percorsi indicati. Aprire una nuova sessione Codex.')
    except Exception:
        if created:
            shutil.rmtree(dest)
        raise

if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as exc:
        print('STOP:', exc, file=sys.stderr)
        sys.exit(1)
