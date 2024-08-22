import datetime 
import locale
import init_Params as ATTRACTIONS
# gestione interfaccia grafica 
import tkinter as tk
from tkinter import ttk

# Librerie Proprietarie
from Algoritmo_Genetico import Genetic_Algorithm
from Greedy_Lib import Greedy
from orologio import Orologio

genetico = Genetic_Algorithm()
greedy = Greedy()
orologio_obj = Orologio()

locale.setlocale(locale.LC_TIME, "it_IT")

# Dati delle attrazioni
Attrazioni = [
    ATTRACTIONS.Acquedotto,
    ATTRACTIONS.Basilica_San_Giorgio,
    ATTRACTIONS.Biblioteca_Ariostea,
    ATTRACTIONS.Casa_Ludovico_Ariosto,
    ATTRACTIONS.Castello_Estense,
    ATTRACTIONS.Chiesa_Gesù,
    ATTRACTIONS.Cimitero_Ebraico,
    ATTRACTIONS.Duomo,
    ATTRACTIONS.Ercole_I_Este,
    ATTRACTIONS.Ghetto_Ebraico,
    ATTRACTIONS.Monastero_S_Antonio,
    ATTRACTIONS.Mura_città,
    ATTRACTIONS.Museo_Archeologico_Nazionale,
    ATTRACTIONS.Museo_Casa_Romei,
    ATTRACTIONS.Museo_Cattedrale,
    ATTRACTIONS.Museo_Risorgimento_Resistenza,
    ATTRACTIONS.Museo_Storia_Naturale,
    ATTRACTIONS.Orto_Botanico,
    ATTRACTIONS.Padiglione_Arte_Contemporanea,
    ATTRACTIONS.Palazzo_Bonacossi,
    ATTRACTIONS.Palazzo_Costabili,
    ATTRACTIONS.Palazzina_Marfisa_Este,
    ATTRACTIONS.Palazzo_Diamanti,
    ATTRACTIONS.Palazzo_Municipale,
    ATTRACTIONS.Palazzo_Schifanoia,
    ATTRACTIONS.Parco_Massari,
    ATTRACTIONS.Parco_Urbano,
    ATTRACTIONS.Piazza_Ariostea,
    ATTRACTIONS.Porta_Paola,
    ATTRACTIONS.Teatro_comunale,
    ATTRACTIONS.Torrione_Barco,
    ATTRACTIONS.Via_Delle_Volte
]
# Dati dell'hotel
Hotel = [
    ATTRACTIONS.Hotel_Annunziata,
    ATTRACTIONS.Hotel_Carlton,
    ATTRACTIONS.Hotel_Europa,
    ATTRACTIONS.Hotel_Orologio,
    ATTRACTIONS.Hotel_Touring
]


def get_days(giorno, data):
    # Input del giorno corrente 
    giorno_corrente = data + datetime.timedelta(days=giorno)
    # Conversione del giorno corrente 
    giorno_corrente = giorno_corrente.strftime("%A")
    return giorno_corrente


# funzione di stampa del percorso
def stampa_tour(tour, giorno_corrente, albergo, ora_inizio, tempo_tot):
    nuovo_orologio = ora_inizio
    # tempo giornaliero
    tempo_restante = tempo_tot*60 
    #punto di partenza
    punto_partenza = albergo
    # conteggio dell'attrazione corrente
    count = 1

    text_area.config(state=tk.NORMAL)

    message = f"\nTour del giorno: {giorno_corrente}"
    text_area.insert(tk.END, message + "\n")
    message = f"Ora Inizio Tour: {ora_inizio}"
    text_area.insert(tk.END, message + "\n")
    message = f"Tempo Disponibile: {tempo_tot}"
    text_area.insert(tk.END, message + "\n")
    message = albergo.nome
    text_area.insert(tk.END, message + "\n") 
    
    for attrazione in tour[1]:
        tempo_visita = attrazione.tempo_visita
        tempo_spostamento = greedy._calcola_spostamento(punto_partenza.posizione, attrazione.posizione)
        message = f"{punto_partenza.nome} -> {attrazione.nome} (Tempo Spostamento (min): {round(tempo_spostamento,2)}')"
        text_area.insert(tk.END, message + "\n")

        message = f"Attrazione_{count}: {attrazione.nome} (Tempo di Visita (min): {attrazione.tempo_visita}')"
        text_area.insert(tk.END, message + "\n")
        tempo_restante -= tempo_visita + tempo_spostamento
        message = f"Tempo Rimanente = {tempo_restante:0.2f}'"
        text_area.insert(tk.END, message + "\n")
        # orologio
        nuovo_orologio = orologio_obj.funzione_orologio(nuovo_orologio, (tempo_visita + tempo_spostamento))
        message = f"Ore: {nuovo_orologio:0.2f}"
        text_area.insert(tk.END, message + "\n")
        punto_partenza = attrazione
        count+=1
    
    message = f"Arrivo a {albergo.nome} alle {orologio_obj.funzione_orologio(nuovo_orologio, greedy._calcola_spostamento(punto_partenza.posizione, albergo.posizione))}"
    text_area.insert(tk.END, message + "\n") 
    message = f"Gradimento del tour: {tour[0]:0.2f}"
    text_area.insert(tk.END, message + "\n\n")
    text_area.config(state=tk.DISABLED)


# Array di copia delle n-attrazioni originali
attrazioni_giornaliere = Attrazioni.copy()
# tour generale della vacanza
tour_vacanza = []
tour_prova = []
gradimento_tot = 0
#start = 0


# funzione di start del programma
def start_function(gradimento_tot, albergo, num_giorni, data, orario, tempo_tot):
    for days in range(num_giorni):
        # setup del giorno corrente
        giorno_corrente = get_days(days, data)
        # verifica delle attrazioni disposnibili al giorno
        attrazioni_verificate = greedy.verifica_attrazione(attrazioni_giornaliere, giorno_corrente)
        # generazione del best tour tramite algoritmo genetico
        best_tour = genetico.genetic_algorithm(attrazioni_verificate, albergo, tempo_tot, orario)
        # stampa del miglio tour giornaliero
        stampa_tour(best_tour, giorno_corrente, albergo, orario, tempo_tot)
        gradimento_tot+=best_tour[0]
        # setup della visita alle attrazioni migliori del giorno
        for attraction in best_tour[1]:
            attraction.visitato = True
    # stampa del gradimento totale del tour in k-giorni
    text_area.config(state=tk.NORMAL)
    message = f"Gradimento TOTALE: {gradimento_tot:0.2f}"
    text_area.insert(tk.END, message + "\n")
    text_area.config(state=tk.DISABLED)


# pulsante di search
def search():
    text_area.delete(1.0, tk.END)
    message = "Calcolo del percorso..."
    text_area.insert(tk.END, message + "\n") 

    data = data_entry.get()
    giorni_vacanza = int(giorni_vacanza_entry.get())
    tempo_tour = float(tempo_tour_entry.get())
    ora_inizio = float(ora_inizio_entry.get())
    hotel = hotel_combobox.get()

   

    data = datetime.datetime.strptime(data, "%Y-%m-%d").date()

    

    if hotel == "Hotel_Annunziata":
        albergo = Hotel[0]
        start_function(gradimento_tot, albergo, giorni_vacanza, data, ora_inizio, tempo_tour)
    elif hotel == "Hotel_Carlton":
        albergo = Hotel[1]
        start_function(gradimento_tot, albergo, giorni_vacanza, data, ora_inizio, tempo_tour)
    elif hotel == "Hotel_Europa":
        albergo = Hotel[2]
        start_function(gradimento_tot, albergo, giorni_vacanza, data, ora_inizio, tempo_tour)
    elif hotel == "Hotel_Orologio":
        albergo = Hotel[3]
        start_function(gradimento_tot, albergo, giorni_vacanza, data, ora_inizio, tempo_tour)
    elif hotel == "Hotel_Touring":
        albergo = Hotel[4]
        start_function(gradimento_tot, albergo, giorni_vacanza, data, ora_inizio, tempo_tour)
    else:
        message = "Hotel non corretto, riprova"
        text_area.insert(tk.END, message + "\n") 


# creazione GUI #
# finestra principale#
main_page = tk.Tk()
main_page.title("TOUR-FE (Ricerca Percorso)")
#main_page.geometry("400x200")

 
# Creazione del widget per la selezione della modalità di viaggio
hotel_label = ttk.Label(main_page, text="Seleziona il tuo Hotel")
hotel_label.grid(row = 4, column = 0)
hotel_label.place()
hotel_combobox = ttk.Combobox(main_page, values=["Hotel_Annunziata", "Hotel_Carlton", "Hotel_Europa", "Hotel_Orologio", "Hotel_Touring"])
hotel_combobox.grid(row = 4, column = 1)
hotel_combobox.current(0)

# Campi di ricerca
data_label = ttk.Label(main_page, text="Data di arrivo (YYYY-MM-GG)")
data_label.grid(row = 0, column = 0, padx=5, pady=5)
data_entry = ttk.Entry(main_page, width=10)
data_entry.grid(row = 0, column = 1, padx=5, pady=5)

giorni_vacanza_label = ttk.Label(main_page, text="Giorni di vacanza")
giorni_vacanza_label.grid(row = 1, column = 0, padx=5, pady=5)
giorni_vacanza_entry = ttk.Entry(main_page, width=5)
giorni_vacanza_entry.grid(row = 1, column = 1, padx=5, pady=5)

tempo_tour_label = ttk.Label(main_page, text="Ore di durata del tour")
tempo_tour_label.grid(row = 2, column = 0, padx=5, pady=5)
tempo_tour_entry = ttk.Entry(main_page, width=5)
tempo_tour_entry.grid(row = 2, column = 1, padx=5, pady=5)

ora_inizio_label = ttk.Label(main_page, text="Ore di inizio del tour")
ora_inizio_label.grid(row = 3, column = 0, padx=5, pady=5)
ora_inizio_entry = ttk.Entry(main_page, width=5)
ora_inizio_entry.grid(row = 3, column = 1, padx=5, pady=5)

# Creazione del pulsante "Cerca"
search_button = ttk.Button(main_page, text="Cerca", command=search)
search_button.grid(row = 5, column = 1)

# Widget di testo per visualizzare i messaggi
text_area = tk.Text(main_page, height=45, width=90)
text_area.grid()



main_page.mainloop()











