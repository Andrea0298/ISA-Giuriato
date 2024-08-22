# Definizione della classe Attrazione
class Attrazione:
    def __init__(self, nome, gradimento, posizione, mattina, pomeriggio, giorno_chiusura
                 , tempo_visita):
        self.nome = nome
        self.gradimento = gradimento
        self.posizione = posizione
        self.mattina = mattina
        self.pomeriggio = pomeriggio
        self.giorno_chiusura = giorno_chiusura
        self.tempo_visita = tempo_visita #minuti
        self.visitato = False  # flag "visitata"

Castello_Estense = Attrazione("Castello Estense", 4.6, (44.8380, 11.6196), (10.00, 12.00), (12.00, 18.00), "martedì", 120)
Palazzo_Diamanti = Attrazione("Palazzo Diamanti", 4.5, (44.8420, 11.6212), (10.00, 12.00), (12.00, 20.00), "lunedì", 90)
Piazza_Ariostea = Attrazione("Piazza Ariostea", 4.5, (44.8413, 11.6226), (00.01, 12.00),(12.00, 24.00), None, 30)
Palazzo_Schifanoia = Attrazione("Palazzo Schifanoia", 4.4, (44.8304, 11.6290), (10.00, 12.00), (12.00, 19.00), "lunedì", 60)
Parco_Urbano = Attrazione("Parco Urbano", 4.5, (44.8524, 11.6206), (00.01, 12.00), (12.00, 24.00), None, 120)
Duomo = Attrazione("Duomo", 4.5, (44.8357, 11.6203), (07.30, 12.30), (15.00, 19.00), None, 60)
Museo_Cattedrale = Attrazione("Museo della Cattedrale", 4.3, (44.8350, 11.6200), (09.30, 13.00), (15.00, 18.00), "lunedì", 70)
Museo_Archeologico_Nazionale = Attrazione("Museo Archeologico Nazionale", 4.6, (44.8274, 11.6272), (09.30, 12.00), (12.00, 17.00), "lunedì", 50)
Ghetto_Ebraico = Attrazione("Ghetto ebraico", 4.5, (44.8339, 11.6209), (00.01, 12.00), (12.00, 24.00), None, 30)
Cimitero_Ebraico = Attrazione("Cimitero ebraico", 4.3, (44.8434, 11.6302), (09.00, 12.00), (12.00, 12.00),  "sabato", 30)
Museo_Casa_Romei = Attrazione("Museo di casa Romei", 4.5, (44.8333, 11.6259), (08.30, 12.00), (12.00, 14.00), None, 120)
Mura_città = Attrazione("Mura di Ferrara", 4.6, (44.8334, 11.6131), (00.01, 12.00), (12.00, 24.00), None, 180)
Torrione_Barco = Attrazione("Torrione del Barco", 4.4, (44.8500, 11.6159), (00.01, 12.00), (12.00, 24.00), None, 25)
Via_Delle_Volte = Attrazione("Via delle Volte", 4.5, (44.8350, 11.6159), (00.01, 12.00), (12.00, 24.00), None, 25)
Ercole_I_Este = Attrazione("Ercole I D'Este", 4.8, (44.8452, 11.6227), (00.01, 12.00), (12.00, 24.00), None, 30)
Monastero_S_Antonio = Attrazione("Monastero di Sant' Antonio", 4.6, (44.8272, 11.6240), (09.30, 11.45), (15.15, 16.45), None, 30)
Palazzo_Municipale = Attrazione("Palazzo Municipale", 4.3, (44.8360, 11.6190), (08.00, 12.00), (12.00, 18.00), "domenica", 60)
Casa_Ludovico_Ariosto = Attrazione("Casa di Ludovico Ariosto", 4, (44.8443, 11.6168), (10.00, 12.00), (12.00, 18.00), "lunedì", 60)
Chiesa_Gesù = Attrazione("Chiesa del Gesù", 4.3, (44.8392, 11.6211), (09.00, 11.30), (17.30, 19.00), None, 45)
Palazzo_Costabili = Attrazione("Palazzo Costabili", 4.8, (44.8274, 11.6272), (09.30, 12.00), (12.00, 17.00), "lunedì", 90)
Parco_Massari = Attrazione("Parco Massari", 4.6, (44.8431, 11.6236), (08.00, 12.00), (12.00, 20.00), None, 60)
Teatro_comunale = Attrazione("Teatro comunale", 4.7, (44.8376, 11.6204), (10.00, 12.00), (12.00, 18.00), None, 60)
Basilica_San_Giorgio = Attrazione("Basilica di San Giorgio", 4.6, (44.8218, 11.6279), (10.00, 12.00), (16.00, 18.00), None, 30)
Museo_Risorgimento_Resistenza = Attrazione("Museo del Risorgimento e della Resistenza", 4.2, (44.8417, 11.6211), (09.30, 13.00), (15.00, 18.00), "mercoledì" , 90)
Museo_Storia_Naturale = Attrazione("Museo di storia naturale", 4.3, (44.8381, 11.6224), (09.30, 13.00), (14.00, 17.00), "sabato", 45)
Padiglione_Arte_Contemporanea = Attrazione("Padiglione di arte contemporanea", 4.3, (44.8422, 11.6239), (10.00, 12.00), (12.00, 18.00), "lunedì", 120)
Palazzo_Bonacossi = Attrazione("Palazzo Bonacossi", 4.4, (44.8318, 11.6291), (0, 0), (14.00, 20.00), "giovedì", 120)
Orto_Botanico = Attrazione("Orto Botanico", 4.2, (44.8418, 11.6223), (09.00, 13.00), (0, 0), "sabato", 30)
Porta_Paola = Attrazione("Porta Paola", 4.4, (44.8322, 11.6167), (09.30, 12.30), (14.30, 17.30), "martedì", 15)
Acquedotto = Attrazione("Acquedotto", 3.7, (44.8376, 11.6080), (00.01, 12.00), (12.00, 24.00), None, 30)
Palazzina_Marfisa_Este = Attrazione("Palazzina Marfisa D'Este", 4.3, (44.8332, 11.6298), (09.30, 13.00), (15.00, 18.00), "venerdì", 30)
Biblioteca_Ariostea = Attrazione("Biblioteca Ariostea", 4.4, (44.8329, 11.6216), (09.30, 12.00), (12.00, 19.00),  "domenica", 60)

# Definizione della classe Albergo
class Hotel:
    def __init__(self, nome, posizione):
        self.nome = nome
        self.posizione = posizione

Hotel_Touring = Hotel("Hotel Touring", (44.8383, 11.6180))
Hotel_Orologio = Hotel("Hotel l'orologio", (44.8354, 11.6056))
Hotel_Carlton = Hotel("Hotel Carlton", (44.8376, 11.6156))
Hotel_Europa = Hotel("Hotel Europa", (44.8371, 11.6222))
Hotel_Annunziata = Hotel("Hotel Annunziata", (44.8370, 11.6182))