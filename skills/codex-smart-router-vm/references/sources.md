# Fonti e verifica — 8 ottobre 2026

Documentazione ufficiale consultata online durante la preparazione:

- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents):
  autorizzazione tramite richiesta, AGENTS.md o skill; tool nativi; modelli
  ereditati; ruoli standalone; precedenza dei modelli configurati.
- [Config Reference](https://learn.chatgpt.com/docs/config-file/config-reference):
  `agents.enabled`, `agents.max_concurrent_threads_per_session`, alias legacy,
  `agents.default_subagent_model`, `agents.default_subagent_reasoning_effort`,
  dichiarazioni `agents.<name>.config_file` e `.description`.
- [Build skills](https://learn.chatgpt.com/docs/build-skills): SKILL.md, discovery
  globale in `~/.agents/skills`, metadati openai.yaml e invocazione implicita.
- [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md): home
  Codex, precedenza AGENTS.override.md, catena di istruzioni e limite dimensione.
- [Models](https://developers.openai.com/api/docs/models): nomi ufficiali Astra,
  Sol e Luna. Catalogo API non equivalente a disponibilità nel client o piano.

CLI locale osservata: 0.162.0-alpha.2. I tool nativi di questa sessione espongono
`gpt-6-astra`, `gpt-6.1-sol`, `gpt-6-sol`, `gpt-6-luna` e selezione del modello.
Questa evidenza non certifica altri account o tutte le versioni Codex.
Non sono inclusi prezzi statici né credenziali. L'installazione proposta non
modifica config.toml. Verificare le capacità effettive dopo aggiornamenti.
