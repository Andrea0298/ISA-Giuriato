# Tour di Ferrara - Algoritmo Genetico

Questo progetto implementa un algoritmo genetico che ha lo scopo di ottimizzare un tour di massimo gradimento tra le attrazioni della città di Ferrara. L'algoritmo seleziona le attrazioni e ne determina l'ordine ottimale per massimizzare il gradimento complessivo del tour, tenendo conto di vari parametri come il tempo disponibile sia per eseguire il tour ogni giorno che come numero di giorni del soggiorno, la data di arrivo, l'orarioin cui ogni giorno si vuole far partire il tour e le preferenze dell'utente sull' albergo.

## Struttura del Progetto

- `src/Algoritmo_Genetico.py`: Implementazione dell'algoritmo genetico con le operazioni di mutazione e crossover tipiche di algoritmi di questo genere.
- `src/Greedy_Lib.py`: Funzione greedy per inizializzare il tour con una soluzione ammissibile.
- `src/init_Params.py`: Gestione dei parametri iniziali per l'algoritmo specificando attrazioni visitabili e possibili hotel.
- `src/main.py`: File principale per eseguire l'algoritmo.
- `src/orologio.py`: Gestione del tempo nel contesto del tour.
- `tests/test_Algoritmo_Genetico.py`: Insieme dei test unitari per le funzioni dell' algoritmo genetico
- `tests/test_Greedy_Lib.py`: Insieme dei test unitari Sulla Greedy che inizializza l'algoritmo
- `tests/integration_test_Algoritmo_Genetico.py`: Test di integarazione per l'algoritmo genetico

## Esecuzione del Progetto

Per eseguire il progetto, assicurati di avere Python installato e tutte le dipendenze soddisfatte.

```bash
pip install -r requirements.txt
python src/main.py
"# ISA" 
