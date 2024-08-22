import random
from Greedy_Lib import Greedy
from orologio import Orologio
# parametri dell'algoritmo
population_size = 50
elite_size = 20
mutation_rate = 0.01
generations = 100
# indici di taglio
start_index = 1
end_index = 3
            

greedy = Greedy()
orologio_obj = Orologio()

class Genetic_Algorithm:

    #funzione di mutazione
    def mutate(self, tour):
        if len(tour) < 2:
            return tour  # Evita la mutazione se il tour ha meno di 2 elementi
        index_a = random.randint(0, len(tour) - 1)
        index_b = index_a
        while index_b == index_a:
            index_b = random.randint(0, len(tour) - 1)
        
        tour[index_a], tour[index_b] = tour[index_b], tour[index_a]
        return tour



    # funzione di cross over
    def crossover(self, parent_a, parent_b, albergo, tempo_restante, orario):
        start_index = 1
        end_index = 3
    
        # Assicurati che start_index ed end_index siano validi
        if start_index < 0:
            start_index = 0
        if end_index >= len(parent_a):
            end_index = len(parent_a) - 1
    
        # Genera i figli combinando le due parti
        def generate_child(p1, p2):
            child = p1[:start_index]
            middle_section = [item for item in p2[start_index:end_index+1] if item not in p1[:start_index] and item not in p1[end_index+1:]]
            child.extend(middle_section)
            child.extend(p1[end_index+1:])
            return child
    
        child_1 = generate_child(parent_a, parent_b)
        child_2 = generate_child(parent_b, parent_a)
    
        # Valuta i figli e seleziona il migliore
        child_evaluations = [self.valuta_tour(child_1, albergo, tempo_restante, orario),
                             self.valuta_tour(child_2, albergo, tempo_restante, orario)]
    
        # Seleziona il miglior bambino basato sul punteggio di valutazione
        best_child = max(child_evaluations, key=lambda attr: attr[0])[1]

        return best_child



    # evoluzione della progenie
    def evolve_population(self, population, elite_size, mutation_rate, albergo, tempo_restante, orario):
        graded_population = [(self.valuta_tour(tour, albergo, tempo_restante, orario)) for tour in population]
        graded_population = sorted(graded_population, key=lambda x: x[0], reverse=True)
        elite = [tour for _, tour in graded_population[:elite_size]]
        offspring = elite.copy()
    
        while len(offspring) < len(population):
            if len(offspring) < 2:
                break  # Non possiamo selezionare due genitori se ci sono meno di due membri
    
            if random.random() < mutation_rate:
                offspring.append(self.mutate(random.choice(offspring)))
            else:
                parent_a, parent_b = random.sample(offspring, 2)
                offspring.append(self.crossover(parent_a, parent_b, albergo, tempo_restante, orario))
    
        return offspring

    

    # algoritmo genetico
    def genetic_algorithm(self, attrazioni_verificate, albergo, tempo_restante, orario):
        population = greedy.genera_popolazione(attrazioni_verificate, albergo, tempo_restante)
        
        for _ in range(generations):
            population = self.evolve_population(population, elite_size, mutation_rate, albergo, tempo_restante, orario)
       
        best_tour = max([(self.valuta_tour(tour, albergo, tempo_restante, orario)) for tour in population], key=lambda attr: attr[0])[0:2]
        return best_tour
    
        


    # funzione di valutazione del tour
    def valuta_tour(self, attrazioni_verificate, albergo, tempo_restante, orario):
        # inizializzazione del tour
        tour_generato = []
        # inizializzazione del punto di partenza
        punto_partenza = albergo
        # inizializzazione dell'orario
        nuovo_orologio = orario
        # inizializzazione del gradimento
        gradimento = 0
        # conversione del tempo restante in minuti
        tempo_restante = float(tempo_restante)*60 # ore -> minuti


        for attrazione in attrazioni_verificate:
            if tempo_restante > 0:
                # setup del tempo di visita dell'attrazione successiva
                tempo_visita = attrazione.tempo_visita 
                # calcolo del tempo di spostamento tra l'attuale e la successiva
                tempo_spostamento = greedy._calcola_spostamento(punto_partenza.posizione, attrazione.posizione)
                # orologio dopo lo spostamento
                nuovo_orologio = orologio_obj.funzione_orologio(nuovo_orologio, tempo_spostamento)
                
                # verifica apertura attrazione e se riesco a visitarla
                if (nuovo_orologio >= attrazione.mattina[0] and nuovo_orologio <= attrazione.mattina[1]): 
                 # verifica apertura dell'attrazione nella mattina
                    if attrazione.mattina[0] != 0 and attrazione.mattina[1] != 0:
                        if nuovo_orologio < attrazione.mattina[0]:
                            if (tempo_visita + tempo_spostamento <= tempo_restante) and (greedy._calcola_spostamento(albergo.posizione, attrazione.posizione) <= tempo_restante-(tempo_visita + tempo_spostamento)): 
                                elapsed_time = nuovo_orologio
                                penality = 0
                                while elapsed_time < attrazione.mattina[0]:
                                    elapsed_time=orologio_obj.funzione_orologio(elapsed_time,2)
                                    penality+= (2/60)
                                tour_generato.append(attrazione)
                                #print(f"Sono trascorsi: {elapsed_time - nuovo_orologio} min")
                                # delta del tempo rimanente
                                tempo_restante -= tempo_visita + tempo_spostamento 
                                # incremento dell'orologio
                                nuovo_orologio = orologio_obj.funzione_orologio(elapsed_time, tempo_visita)
                                #print(f"Visitata {attrazione.nome} alle: {nuovo_orologio}") 
                                # assegnazione gradimento
                                gradimento+=(attrazione.gradimento - penality)
                                # assegnazione del nuovo punto di partenza
                                punto_partenza = attrazione
                    
                        elif (tempo_visita + tempo_spostamento <= tempo_restante) and (greedy._calcola_spostamento(albergo.posizione, attrazione.posizione) <= tempo_restante-(tempo_visita + tempo_spostamento)): 
                            tour_generato.append(attrazione)
                            # delta del tempo rimanente
                            tempo_restante -= tempo_visita + tempo_spostamento 
                            # incremento dell'orologio
                            nuovo_orologio = orologio_obj.funzione_orologio(nuovo_orologio, tempo_visita)
                            # assegnazione gradimento
                            gradimento+=attrazione.gradimento
                            # assegnazione del nuovo punto di partenza
                            punto_partenza = attrazione
                            
                        
                
                # verifica apertura attrazione e se riesco a visitarla
                elif (nuovo_orologio >= attrazione.pomeriggio[0] and nuovo_orologio <= attrazione.pomeriggio[1]): 
                # verifica apertura dell'attrazione nel pomeriggio
                    if attrazione.pomeriggio[0] != 0 and attrazione.pomeriggio[1] != 0:
                            if nuovo_orologio < attrazione.pomeriggio[0]:
                                if (tempo_visita + tempo_spostamento <= tempo_restante) and (greedy._calcola_spostamento(albergo.posizione, attrazione.posizione) <= tempo_restante-(tempo_visita + tempo_spostamento)): 
                                    elapsed_time = nuovo_orologio
                                    penality = 0
                                    while elapsed_time < attrazione.pomeriggio[0]:
                                        elapsed_time=orologio_obj.funzione_orologio(elapsed_time,2)
                                        penality+= (2/60)
                                    tour_generato.append(attrazione)
                                    # delta del tempo rimanente
                                    tempo_restante -= tempo_visita + tempo_spostamento 
                                    # incremento dell'orologio
                                    nuovo_orologio = orologio_obj.funzione_orologio(elapsed_time, tempo_visita)
                                    # assegnazione gradimento
                                    gradimento+=(attrazione.gradimento - penality)
                                    # assegnazione del nuovo punto di partenza
                                    punto_partenza = attrazione
                            
                            elif (tempo_visita + tempo_spostamento <= tempo_restante) and (greedy._calcola_spostamento(albergo.posizione, attrazione.posizione) <= tempo_restante-(tempo_visita + tempo_spostamento)): 
                                tour_generato.append(attrazione)
                                # delta del tempo rimanente
                                tempo_restante -= tempo_visita + tempo_spostamento 
                                # incremento dell'orologio
                                nuovo_orologio = orologio_obj.funzione_orologio(nuovo_orologio, tempo_visita)
                                #print(f"Visitata il pomeriggio: {punto_partenza.nome} alle {nuovo_orologio}")
                                # assegnazione gradimento
                                gradimento+=attrazione.gradimento
                                # assegnazione del nuovo punto di partenza
                                punto_partenza = attrazione
                        
            else:
                break
                        
        return gradimento, tour_generato