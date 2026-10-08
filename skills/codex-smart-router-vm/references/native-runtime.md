# Due superfici native

Lo schema dei tool della sessione è autoritativo: non confondere nomi dei tool,
parametri JSON e chiavi TOML. Non assumere che ogni client esponga lo stesso tool.

## Tool con selezione diretta del modello

Se `collaboration.spawn_agent` espone `task_name`, `message`, `model`,
`reasoning_effort`, `fork_turns`, usa questi parametri. Un fork completo può
imporre ereditarietà: per selezionare modello/effort usa `fork_turns="none"` e un
brief autosufficiente, oppure un numero di turni se lo schema lo permette.
Attendi tramite gli strumenti collaboration disponibili e raccogli l'esito.
Non creare chat laterali tramite `create_thread`.

Esempio solo per tale schema e modello verificato disponibile:
```json
{"task_name":"scan","model":"gpt-6-luna","reasoning_effort":"high","fork_turns":"none","message":"Esamina in sola lettura i file indicati nel brief. Restituisci punti di ingresso e riferimenti. Non delegare ulteriormente."}
```
Aggiungi al messaggio i percorsi e il contesto concreto del compito.

## Client con agenti personalizzati

La documentazione corrente supporta file TOML standalone in `~/.codex/agents/`
(o nella home Codex del profilo) e `.codex/agents/` nel progetto. Ogni file
contiene `name`, `description`, `developer_instructions`; può impostare `model`
e `model_reasoning_effort`. I template in `templates/agents/` sono esempi pronti,
ma si installano solo per modelli verificati disponibili. Se il tool espone
`agent_type`, seleziona il nome del ruolo solo se riconosciuto dal runtime.
Se non espone un selettore di ruoli, usa la superficie diretta o il fallback.

Un modello fissato nel file agente prevale sullo spawn e sui default: non usare
un ruolo Astra indisponibile cercando di correggerlo con un override dello spawn.
Scegli un ruolo diverso o l'esecuzione diretta.

`agents/openai.yaml` dentro la skill contiene metadati UI: non configura modelli.
`templates/config.example.toml` è un esempio globale opzionale, mai da copiare
sopra un config esistente. Le chiavi correnti sono `agents.enabled` e
`agents.max_concurrent_threads_per_session`; `agents.max_threads` è legacy.
Non aggiungere per abitudine `features.multi_agent` alle versioni correnti.
Il router funziona senza modificare config.toml se i tool sono già disponibili.
