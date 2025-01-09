print ('esercizio in python con Stack')

# creo classe Comunicazione con due attr mittente e messaggio

# class Comunicazione():
#     def __init__(self, mittente,messaggio):
#         self.mittente = mittente
#         self.messaggio = messaggio

#     def __str__(self):
#         return f"Da {self.mittente}: {self.messaggio}"

from dataclasses import dataclass
# creo classe Comunicazione con due attr mittente e messaggio usando dataclass
@dataclass
class Comunicazione:
    mittente: str
    messaggio: str

    def __str__(self):
        return f"Da {self.mittente}: {self.messaggio}"



# creo classe stack per raggruppare i messaggi

class StackComunicazioni:
    def __init__(self, capacita=10):
        self.comunicazioni = []
        self.capacita = capacita

    def push(self, comunicazione):
        if len(self.comunicazioni) >= self.capacita:
            raise OverflowError("Stack pieno!")
        self.comunicazioni.append(comunicazione)
        print(f"\nAggiunto messaggio: {comunicazione}")

    def pop(self):
        if not self.comunicazioni:
            raise IndexError("Stack vuoto!")
        return self.comunicazioni.pop()
        

# Test
stack = StackComunicazioni(4)

com1 = Comunicazione("Nettuno", "Ciao!")
com2 = Comunicazione("Marte", "Ciao!")
com3 = Comunicazione("Plutone", "Ciao!")

stack.push(com1)
stack.push(com2)
stack.push(com3)

print(f"\nRimosso messaggio: {stack.pop()}")
print(f"\nRimosso messaggio: {stack.pop()}")
print(f"\nRimosso messaggio: {stack.pop()}")

