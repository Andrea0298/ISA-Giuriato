import pytest
import sys
import os

# Aggiungi la cartella src al percorso di ricerca dei moduli
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from Algoritmo_Genetico import Genetic_Algorithm
from Greedy_Lib import Greedy
from orologio import Orologio

# Oggetti di test per attrazioni
class Attrazione:
    def __init__(self, nome, posizione, tempo_visita, gradimento, mattina, pomeriggio):
        self.nome = nome
        self.posizione = posizione
        self.tempo_visita = tempo_visita
        self.gradimento = gradimento
        self.mattina = mattina
        self.pomeriggio = pomeriggio

# Setup per i test di integrazione
@pytest.fixture
def setup_data():
    albergo = Attrazione("Albergo", (0, 0), 0, 0, (0, 0), (0, 0))
    attrazioni = [
        Attrazione("Museo", (2, 3), 60, 8, (9, 12), (14, 18)),
        Attrazione("Parco", (5, 8), 90, 7, (10, 13), (15, 19)),
        Attrazione("Teatro", (10, 10), 120, 9, (9, 12), (16, 22)),
    ]
    orario = 9  # Orario di partenza alle 9:00
    tempo_restante = 8  # 8 ore disponibili per il tour
    return attrazioni, albergo, tempo_restante, orario

def test_genetic_algorithm(setup_data):
    attrazioni_verificate, albergo, tempo_restante, orario = setup_data
    ga = Genetic_Algorithm()
    
    # Esegui l'algoritmo genetico
    best_tour = ga.genetic_algorithm(attrazioni_verificate, albergo, tempo_restante, orario)
    
    # Verifica che il risultato sia coerente
    assert isinstance(best_tour, tuple)
    assert isinstance(best_tour[0], (int, float))  # Il gradimento dovrebbe essere un numero
    assert isinstance(best_tour[1], list)  # Il tour generato dovrebbe essere una lista
    assert all(isinstance(attrazione, Attrazione) for attrazione in best_tour[1])  # Controlla se gli elementi nel tour sono attrazioni

    # Controlla che il gradimento sia positivo
    assert best_tour[0] >= 0

