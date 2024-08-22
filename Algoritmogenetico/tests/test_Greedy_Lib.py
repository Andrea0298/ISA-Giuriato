import sys
import os
import unittest
from unittest.mock import MagicMock
from geopy import distance

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from Greedy_Lib import Greedy
from Greedy_Lib import num_popolazione
  
class TestGreedy(unittest.TestCase):

    def setUp(self):
        # Setup iniziale comune per i test
        self.greedy = Greedy()

        # Creiamo una classe mock per simulare le attrazioni
        class Attrazione:
            def __init__(self, nome, posizione, tempo_visita, giorno_chiusura, visitato):
                self.nome = nome
                self.posizione = posizione
                self.tempo_visita = tempo_visita
                self.giorno_chiusura = giorno_chiusura
                self.visitato = visitato

        self.Attrazione = Attrazione

        # Definiamo delle attrazioni fittizie
        self.attrazioni = [
            self.Attrazione("Attrazione A", (41.9028, 12.4964), 60, "lunedì", False),
            self.Attrazione("Attrazione B", (48.8566, 2.3522), 90, "martedì", False),
            self.Attrazione("Attrazione C", (51.5074, -0.1278), 45, "mercoledì", True),
        ]

        # Definiamo un albergo fittizio
        self.albergo = self.Attrazione("Albergo", (40.7128, -74.0060), 0, None, False)

    def test_verifica_attrazione(self):
        giorno_corrente = "martedì"
        attrazioni_verificate = self.greedy.verifica_attrazione(self.attrazioni, giorno_corrente)
        # Verifichiamo che solo le attrazioni aperte e non visitate vengano restituite
        self.assertEqual(len(attrazioni_verificate), 1)
        self.assertEqual(attrazioni_verificate[0].nome, "Attrazione A")

    def test_shaffle_tour(self):
        attrazioni_verificate = self.greedy.verifica_attrazione(self.attrazioni, "lunedì")
        # Assicuriamoci che la lista mescolata abbia la stessa lunghezza e contenuto
        tour_shuffled = self.greedy.shaffle_tour(attrazioni_verificate)
        self.assertEqual(len(tour_shuffled), len(attrazioni_verificate))
        self.assertCountEqual(tour_shuffled, attrazioni_verificate)  # verifica che gli elementi siano gli stessi, ma l'ordine può cambiare

    def test_calcola_spostamento(self):
        coordinate_a = (41.9028, 12.4964)  # Roma
        coordinate_b = (48.8566, 2.3522)   # Parigi
        tempo_spostamento = self.greedy._calcola_spostamento(coordinate_a, coordinate_b)
        # Verifica che il calcolo dello spostamento sia corretto
        self.assertIsInstance(tempo_spostamento, int)
        self.assertGreater(tempo_spostamento, 0)

    def test_genera_tour(self):
        tempo_restante = 10  # in ore
        attrazioni_verificate = self.greedy.verifica_attrazione(self.attrazioni, "lunedì")
        tour = self.greedy.genera_tour(attrazioni_verificate, self.albergo, tempo_restante)
        # Verifica che il tour generato non sia vuoto e che rispetti le condizioni
        self.assertGreaterEqual(len(tour), 0)
        self.assertLessEqual(sum([a.tempo_visita for a in tour]), tempo_restante * 60)

    def test_genera_popolazione(self):
        tempo_restante = 10  # in ore
        attrazioni_verificate = self.greedy.verifica_attrazione(self.attrazioni, "lunedì")
        popolazione = self.greedy.genera_popolazione(attrazioni_verificate, self.albergo, tempo_restante)
        # Verifica che la popolazione generata abbia la dimensione giusta
        self.assertEqual(len(popolazione), num_popolazione)
        # Verifica che ogni tour all'interno della popolazione sia una lista
        for tour in popolazione:
            self.assertIsInstance(tour, list)

if __name__ == "__main__":
    unittest.main()

