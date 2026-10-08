---
name: codex-smart-router-vm
description: Instrada attività Codex articolate tra esecuzione diretta e subagent nativi con selezione cost-aware dei modelli disponibili. Usa per implementazioni, pianificazione complessa, esplorazioni o test delegabili e quando AGENTS.md richiede il router; gestisci direttamente richieste semplici.
---

# Codex Smart Router VM

`vm` sono iniziali personali: nessun flag `-vm`, macchina virtuale o modalità speciale.
Questa skill richiede esplicitamente delegazione nativa quando utile secondo la
politica seguente. Non richiede delegazione per ogni richiesta. Caveman è separata.
Non cambiare il modello della chat principale, account, permessi o configurazione.

## Decisione ed esecuzione

1. Rispetta istruzioni utente e progetto e usa le skill specialistiche pertinenti.
   Se sei già un subagent, completa il solo incarico ricevuto senza ulteriore
   delegazione, salvo richiesta esplicita del coordinatore.
2. Per un compito semplice, dipendenze strettamente sequenziali o un contesto
   costoso da trasferire, procedi direttamente. Prima di delegare leggi
   [routing-policy.md](references/routing-policy.md).
3. Verifica strumenti nativi, autorizzazione, slot, modelli e livelli di reasoning
   realmente esposti dal runtime. Un nome nel catalogo API o nei template non
   prova accesso nell'account. Se mancano prove, usa il modello ereditato soltanto
   se la delegazione conserva un vantaggio concreto; altrimenti esecuzione diretta.
4. Preferenze, esclusivamente se disponibili:
   - planner: Astra (`gpt-6-astra`) per incertezza e decisioni architetturali difficili;
   - developer: Sol (`gpt-6.1-sol`; `gpt-6-sol` se è il Sol disponibile);
   - explorer/tester: Luna (`gpt-6-luna`) per ricerca circoscritta e test definiti.
   Sono preferenze, non una pipeline obbligatoria. Non inventare alias o accesso.
5. Delega con gli strumenti nativi realmente presenti. Leggi
   [native-runtime.md](references/native-runtime.md) per adattare la chiamata.
   Usa il minimo numero di agenti: normalmente uno, al massimo due contemporanei
   per questa politica e comunque entro gli slot disponibili. Nessun router esterno,
   chiamata API, nuovo chat utente o processo `codex exec` come sostituto.
6. Specifica obiettivo, evidenze di partenza, file autorizzati, vincoli, criterio
   di accettazione, budget qualitativo e risultato atteso. Passa solo il contesto
   necessario. Assegna un solo proprietario per ogni file modificato. Un tester
   non deve operare su file che stanno ancora cambiando: aspetta la consegna.
7. Attendi e verifica i risultati; integra le modifiche e completa le verifiche
   pertinenti. Non rifare automaticamente l'intero lavoro del subagent. Se fallisce
   il modello o il tool, comunica il limite e applica il fallback documentato.

## Report

Concludi con una nota breve: modalità diretta/delegata e motivo; ruoli e modelli
richiesti, modelli effettivamente confermati oppure identità non verificata;
risultati dei controlli e fallback. Token e costi solo se misurati, altrimenti
«costo non misurato». Nessuna promessa di risparmio o percentuale inventata.

Per installazione e configurazione vedi [INSTALL.md](INSTALL.md).
Fonti e limiti verificati: [sources.md](references/sources.md).
