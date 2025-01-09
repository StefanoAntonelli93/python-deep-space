print('esercizio con singleton pattern')

# creo classe computer centrale
class ComputerCentrale:
    _istanza = None
    # istanza privata

    # creo costruttore dove se istanza è none ne creo una

    def __new__(cls):
        if cls._istanza is None:
            cls._istanza = super().__new__(cls)
            cls._istanza.stato = "in attesa"
            cls._istanza.motori = "spenti"
        return cls._istanza
    
    # creo metodi d'istanza

    def statoAstronave(self):
        return f"Stato MilleniumFalco: {self.stato}, Motori: {self.motori}"
    
    def avvioMotori(self):
        self.motori = "accesi"
        self.stato = "in movimento"

    def spegniMotori(self):
        self.motori = "spenti"
        self.stato = "in attesa"  

# creo due computer

computer1 = ComputerCentrale()
computer2 = ComputerCentrale()

# se true allora le due variabili puntano allo stesso oggetto = SINGLETON
print(computer1 == computer2)

print(computer1.statoAstronave())

computer1.avvioMotori()
print(computer2.statoAstronave())

computer2.spegniMotori()
print(computer1.statoAstronave())

