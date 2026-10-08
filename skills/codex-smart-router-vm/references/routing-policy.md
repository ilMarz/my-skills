# Politica cost-aware

Valuta il lavoro residuo, non il costo già sostenuto. Un modello meno caro non
rende automaticamente economica la delegazione. Considera contesto duplicato,
istruzioni di avvio, output, tool, attese, revisione, integrazione e rischio di
rilavorazione. Il tempo risparmiato in parallelo è distinto dai token risparmiati.

Se prezzi e uso sono osservabili:
C_delega = C_coordinamento + somma(C_input + C_output + C_tool dei figli)
           + C_revisione + C_rilavorazione_attesa.
Confronta con C_diretto residuo, includendo token cached solo se misurati.
Per abbonamenti Codex non equiparare prezzi API e consumo del piano.
Senza misure usa un confronto qualitativo, non valori monetari inventati.

Delega solo con risultato separabile e almeno un vantaggio plausibile: riduzione
netta del lavoro del coordinatore, parallelismo indipendente significativo,
oppure qualità necessaria che giustifica costo superiore. In quest'ultimo caso
esplicita che la scelta privilegia qualità e non presume risparmio.

- Correzione di una riga o singola ricerca: diretto.
- Scansione ampia ma circoscritta, indipendente: Luna, se trasferimento e verifica
  costano meno della scansione nel coordinatore.
- Implementazione da criteri chiari: Sol, se delegabile senza continui handoff.
- Decisione architetturale ambigua e costosa da sbagliare: Astra per un piano
  circoscritto; il coordinatore decide e assegna solo dopo l'esito.
- Test definiti su artefatto stabile: Luna; risultati con comando, esito e limiti.
- Test o analisi che richiedono ragionamento profondo: Sol o Astra se necessario,
  mai Luna soltanto per rispettare l'etichetta del ruolo.

Usa reasoning supportato: punto di partenza low per planner Astra, medium per
Sol, high per Luna; adegua a difficoltà e costo. Non forzare ultra/max.
Se il coordinatore ha già modello e contesto adatti, evita un agente equivalente.

Fallback: modello richiesto assente → altra versione della stessa famiglia
esplicitamente disponibile → modello corrente ereditato se conveniente → diretto.
Non tentare nomi casuali. Un errore di disponibilità autorizza al massimo un
nuovo tentativo con alternativa verificata; poi diretto. Per errori transitori
valuta un singolo retry. Per budget esaurito/permessi negati non riprovare per
aggirare il limite. Interrompi lavoro ridondante solo con tool supportati.
Il limite normale di due figli simultanei non autorizza un numero illimitato di
ondate: rivaluta prima di ciascuna e riusa un figlio se ha già il contesto utile.
