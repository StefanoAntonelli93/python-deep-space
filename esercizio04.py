print ('esercizio con linked list')

# creo classe Pianeta

class Pianeta():
    def __init__(self,nome):
        self.nome = nome
        self.successivo = None

# creo classe Linked

class LinkedListPianeti():
    def __init__(self):
        self.head = None

    def aggiungi_pianeta(self, nome_pianeta):
        nuovo_pianeta = Pianeta(nome_pianeta)
        # se lista è vuota aggiungo primo pianeta e ritorno altrimenti cerco dalla testa della lista il primo pianeta e aggiungo gli altri
        if self.head is None:
            self.head = nuovo_pianeta
            return
        ultimo_pianeta = self.head
        while ultimo_pianeta.successivo:
            ultimo_pianeta = ultimo_pianeta.successivo
        ultimo_pianeta.successivo = nuovo_pianeta


    def visualizza_pianeti(self):
        pianeta_corrente = self.head
        # finchè esite un pianeta stampo pianeta corrente poi passo al successivo e lo stampo, quando finisce la lista stampo fine lista
        while pianeta_corrente:
            print(pianeta_corrente.nome, end=" -> ")
            pianeta_corrente = pianeta_corrente.successivo
        print("Fine Lista")
    


lista_pianeti = LinkedListPianeti()

lista_pianeti.aggiungi_pianeta("Marte")
lista_pianeti.aggiungi_pianeta("Venere")
lista_pianeti.aggiungi_pianeta("Giove")

lista_pianeti.visualizza_pianeti()
