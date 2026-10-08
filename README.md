# my-skills

Raccolta personale delle skill Codex di Valerio Marzulli (`ilMarz`).

## Skill disponibili

| Skill | Scopo | Installazione |
| --- | --- | --- |
| [codex-smart-router-vm](skills/codex-smart-router-vm/SKILL.md) | Routing tra esecuzione diretta e subagent nativi, con attenzione a disponibilità dei modelli, costi e overhead. | [Guida Mac](skills/codex-smart-router-vm/INSTALL.md) |

## Organizzazione

Ogni skill vive in `skills/<nome-skill>/`, con il proprio `SKILL.md` e le risorse necessarie. I sorgenti sono versionati; gli archivi generati possono essere salvati in `dist/`, esclusa da Git.

Aggiungere solo skill selezionate per questa raccolta personale. Non includere credenziali, dati cliente o materiali di lavoro riservati. Il suffisso `-vm` indica iniziali personali, non un flag di invocazione. Caveman resta una skill separata.

## Installazione

Clonare questo repository non installa le skill. Per il router, dalla radice del repository:

```sh
python3 skills/codex-smart-router-vm/scripts/install.py
python3 skills/codex-smart-router-vm/scripts/install.py --apply
```

Il primo comando mostra l'anteprima. Consultare la guida della singola skill per requisiti, gestione dei file esistenti e verifiche.
