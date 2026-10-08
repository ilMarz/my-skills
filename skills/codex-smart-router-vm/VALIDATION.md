# Validazione — 8 ottobre 2026

Pacchetto preparato e verificato localmente su macOS, Python 3.9.6.
Nessuna installazione nell'account reale: tutte le prove dell'installer hanno
usato home temporanee isolate nella cartella di lavoro.

Controlli eseguiti con esito positivo:

- Validatore `quick_validate.py` della skill-creator: `Skill is valid!`.
- Parsing YAML di metadati e frontmatter; invocazione implicita abilitata.
- Parsing dei cinque file TOML; campi obbligatori dei quattro ruoli presenti.
- Link relativi da SKILL.md e riferimenti risolti, inclusa INSTALL.md.
- Anteprima installer senza scritture; installazione nuova; seconda esecuzione
  idempotente; preservazione byte per byte delle istruzioni precedenti e backup.
- config.toml preesistente invariato anche con agenti disabilitati.
- Collisioni skill, duplicati legacy, blocco marcato incompleto e override attivo
  rilevati senza modificare i file preesistenti.
- Integrità ZIP, estrazione e ripetizione del validatore sul contenuto estratto.

Revisione comportamentale indipendente tramite subagent nativo Codex, con
`gpt-6-luna` richiesto, `high`, fork senza cronologia. Il runtime ha accettato
la chiamata e restituito la revisione; il risultato non espone telemetria
separata che attesti il modello effettivo. Token/costo non misurati.

Sei scenari valutati in simulazione:

| Scenario | Decisione osservata |
| --- | --- |
| Refuso singolo | Diretto |
| Architettura ambigua con Astra disponibile | Piano circoscritto Astra se giustificato |
| Due componenti indipendenti, Luna disponibile | Uno o due Luna secondo overhead |
| Luna assente, solo modello corrente | Ereditarietà solo se conveniente, altrimenti diretto |
| Tool multiagent assenti | Diretto con limite dichiarato |
| Due scrittori sullo stesso file | Proprietario unico o sequenza delle modifiche |

La revisione aveva segnalato un link INSTALL.md non ancora creato durante la
lettura concorrente e uno spazio superfluo nel frammento: entrambi risolti e
link verificato sul pacchetto completo.

Limiti: nessun collaudo live di spawn Astra/Sol; nessuna installazione live dei
ruoli o certificazione di compatibilità con ogni versione/account. La sintassi
è confrontata con le fonti ufficiali elencate in references/sources.md e
analizzata come TOML, non caricata in un nuovo runtime Codex. Le simulazioni
non sono benchmark di risparmio. Auto-attivazione dopo installazione da
verificare in una nuova sessione come indicato in INSTALL.md.
