from geopy import distance
import random

num_popolazione = 100

class Greedy:

    # funzione che genera n-tour iniziali detti "popolazione"
    def genera_popolazione(self, attrazioni_verificate, albergo, tempo_restante):
        popolazione = []

        # prima iterazione della generazione
        popolazione.append(self.genera_tour(attrazioni_verificate, albergo, tempo_restante))
        attrazioni_verificate = self.shaffle_tour(attrazioni_verificate)

        for _ in range(num_popolazione - 1):
            popolazione.append(self.genera_tour(attrazioni_verificate, albergo, tempo_restante))
            attrazioni_verificate = self.shaffle_tour(attrazioni_verificate)

        return popolazione


        
    def genera_tour(self, attrazioni_verificate, albergo, tempo_restante):
        tour_generato = []
        punto_partenza = albergo
        # conversione del tempo restante in minuti
        tempo_restante = float(tempo_restante)*60 # ore -> minuti


        for attrazione in attrazioni_verificate:
            # setup del tempo di visita dell'attrazione successiva
            tempo_visita = attrazione.tempo_visita 
            # calcolo del tempo di spostamento tra l'attuale e la successiva
            tempo_spostamento = self._calcola_spostamento(punto_partenza.posizione, attrazione.posizione)

            if tempo_restante > 0:
                if tempo_visita + tempo_spostamento < tempo_restante and self._calcola_spostamento(albergo.posizione, attrazione.posizione) < tempo_restante - (tempo_visita + tempo_spostamento):
                    tour_generato.append(attrazione)
                    # delta del tempo rimanente
                    tempo_restante -= tempo_visita + tempo_spostamento 
                    punto_partenza = attrazione
            else:
                break

        return tour_generato
    
    # generazione di una nuova lista di attrazioni
    def shaffle_tour(self, attrazioni_verificate):
        tour = list(attrazioni_verificate)
        random.shuffle(tour)
        return tour

    # calcolo del tempo di spostamento
    def _calcola_spostamento(self, coordinate_a, coordinate_b):
        tempo_spostamento = ((distance.distance(coordinate_a, coordinate_b).km)/5)*60 #min
        tempo_spostamento = int(tempo_spostamento) #min
        return tempo_spostamento
    

    # Funzione di verifica dell'attrazione in base a:
    # - giorno di apertura
    # - visitata si/no
    def verifica_attrazione(self, attrazioni, giorno_corrente):
        attrazioni_verificate = []
        #print(giorno_corrente)
        for element in attrazioni:
            if (element.giorno_chiusura != giorno_corrente) and (element.visitato == False):
                attrazioni_verificate.append(element)
            
        return attrazioni_verificate
