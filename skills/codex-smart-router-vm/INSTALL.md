# Installazione globale su Mac

Questo archivio è un pacchetto da installare; la consegna non installa nulla.
Richiede Python 3.9+ e un client Codex con skills. Nessuna dipendenza Python esterna.

1. Estrai `skill.zip` in una cartella vuota, ad esempio `~/Downloads/router-vm`.
2. Apri Terminale nella cartella estratta ed esegui:

```sh
python3 codex-smart-router-vm/scripts/install.py
python3 codex-smart-router-vm/scripts/install.py --apply
```

Il primo comando mostra il piano; il secondo installa la skill in
`~/.agents/skills/codex-smart-router-vm` e aggiunge un blocco marcato in coda a
`${CODEX_HOME:-$HOME/.codex}/AGENTS.md`, mantenendo i byte precedenti e creando
un backup univoco. Non riscrive config.toml, non cambia account o modello della
chat. L'installer non copia agenti con modelli potenzialmente indisponibili.
Non eseguire mentre altri processi stanno modificando queste destinazioni.

Una seconda esecuzione identica non duplica dati. Una skill omonima diversa,
un blocco già modificato o un AGENTS.override.md attivo causano arresto senza
modifiche: confronta manualmente e integra `templates/AGENTS.fragment.md` nel
file realmente caricato, preservandone il contenuto. Non eliminare override
soltanto per far funzionare il router. Con `CODEX_HOME` personalizzato controlla
il percorso mostrato; la discovery user delle skill resta in `~/.agents/skills`.
Le installazioni legacy in `.codex/skills` non vanno duplicate.

## Configurazione nativa opzionale

Se il runtime espone spawn con selezione di modello, basta la skill installata.
Se supporta ruoli TOML standalone, verifica prima i modelli realmente disponibili
nel selettore o nei metadati dei tool. Copia solo i template dei ruoli compatibili
in `${CODEX_HOME:-$HOME/.codex}/agents/` con nomi `vm_planner.toml`,
`vm_developer.toml`, `vm_explorer.toml`, `vm_tester.toml`, senza sostituire file
esistenti. Esempio per il solo planner, dopo aver verificato Astra:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/agents"
cp -n codex-smart-router-vm/templates/agents/vm_planner.toml "${CODEX_HOME:-$HOME/.codex}/agents/"
```

I template usano Astra `gpt-6-astra`, Sol `gpt-6.1-sol`, Luna `gpt-6-luna`.
Se è disponibile solo `gpt-6-sol`, adatta il template developer prima della copia.
Non registrare ruoli che fissano modelli non disponibili. Il router può lavorare
con modello ereditato o direttamente. Non serve abilitare feature legacy.

`templates/config.example.toml` illustra le chiavi correnti facoltative:
`agents.enabled` e `agents.max_concurrent_threads_per_session`. Non copiare il
file sopra config.toml e non aggiungere una seconda tabella `[agents]` se esiste.
Integra soltanto chiavi desiderate e assenti, dopo backup; conserva eventuali
limiti più restrittivi. Nessuna modifica di configurazione è necessaria se i
tool nativi sono già presenti. Client vecchi possono non supportare questo
schema: aggiornare consapevolmente o usare il fallback diretto.

## Verifica dopo installazione

Apri una nuova chat/sessione. Chiedi di elencare le istruzioni attive e verificare
che `codex-smart-router-vm` sia leggibile. Se manca, riavvia Codex e controlla
skill disabilitate, profilo, override e limiti della catena AGENTS.md.
Auto-attivazione è una direttiva per Codex, non un hook deterministico: le
istruzioni di priorità superiore e quelle locali possono limitarla.

Prova prima «Correggi questo refuso»: ci si aspetta esecuzione diretta.
Poi assegna due analisi indipendenti abbastanza ampie: se conveniente ci si
aspetta delegazione, risultati verificati e report con modelli confermati o
incertezza dichiarata. L'invocazione esplicita è `$codex-smart-router-vm`;
`-vm` non è un argomento da aggiungere ai comandi. Caveman non viene installata.

## Rimozione o aggiornamento

Per rimuovere, elimina solo la cartella della skill e il blocco compreso tra
`codex-smart-router-vm:begin` e `codex-smart-router-vm:end` nel file istruzioni.
Elimina solo eventuali ruoli `vm_*` che hai copiato e che non usi altrove.
Non ripristinare ciecamente un backup se nel frattempo hai aggiunto altre
istruzioni. Per aggiornare, confronta le cartelle e conserva le personalizzazioni;
l'installer rifiuta deliberatamente di sovrascrivere versioni diverse.
