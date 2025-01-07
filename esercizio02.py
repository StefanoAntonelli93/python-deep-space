print ("esercizio 2")
# creo classe pianeta
class Pianeta:
    def __init__(self, nome, risorse):
        self.nome = nome
        self.risorse = risorse

 
# creo classe astronave con inizializzatore per capacita di carico
class Astronave:
    def __init__(self, capacita_carico):
        self.capacita_carico = capacita_carico
        self.carico_attuale = 0
        self.risorse_raccolte = {}
    # creo metodo statico per messaggio di esplorazione
    @staticmethod
    def messaggio_esplorazione(nome_pianeta):
        return f"L'astronave sta esplorando il pianeta {nome_pianeta}."
    # creo metodo di classe per astronave standard
    @classmethod
    def astronave_standard(cls):
        return cls(capacita_carico = 300)
    # creo metodo di istanza capacita rimanente
    def capacita_rimanente(self):
        return self.capacita_carico - self.carico_attuale
    # creo metodo privato
    def _puo_caricare(self, massa):
        return self.carico_attuale + massa <= self.capacita_carico
    # creo metodo esplora
    def esplora(self, pianeta):
        print(Astronave.messaggio_esplorazione(pianeta.nome))

        for risorsa, massa in pianeta.risorse.items():
            if self._puo_caricare(massa):
                self.carico_attuale += massa
                self.risorse_raccolte[risorsa] = self.risorse_raccolte.get(risorsa, 0) + massa
                print(f"Raccolta la risorsa {risorsa} con massa {massa}!")
            else:
                print(f"Impossibile raccogliere ulteriormente {risorsa} a causa della capacità di carico!")

        

# creo nuovi pianeti e le loro risorse

terra = Pianeta("Terra", {'ferro': 50, 'oro': 25})
marte = Pianeta("Marte", {'ferro': 30, 'argento': 40})
giove = Pianeta("Giove", {'platino': 90, 'oro': 120})
saturno = Pianeta("Saturno", {'oro' : 30, 'ferro': 20, 'argento':10})


# creo astronave usando il classmethod

milleniumFalco = Astronave.astronave_standard()

# astronave esplora i pianeti e raccolgie risorse

milleniumFalco.esplora(terra)
milleniumFalco.esplora(marte)
milleniumFalco.esplora(giove)
milleniumFalco.esplora(saturno)

print("\nRisorse raccolte dall'astronave:")
for risorsa, massa in milleniumFalco.risorse_raccolte.items():
    print(f"{risorsa}: {massa} tonnellate")
