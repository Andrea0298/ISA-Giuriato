
class Orologio:

    def funzione_orologio(self, orologio, tempo_spost):
        orologio_ore = int(orologio)
        orologio_min = int(round(float(orologio - orologio_ore),2)*100)

        min_totali = float(orologio_min + tempo_spost)
       
        if min_totali >= 60:
            while(min_totali >= 60):
                orologio_ore+=1
                min_totali-=60

        min_totali = round(min_totali/100, 2)
       
        orologio = float(orologio_ore + min_totali)
       
        return orologio
    
    
            

