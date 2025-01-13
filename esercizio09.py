#  design pattern COMPOSITE

from abc import ABC, abstractmethod

# creo classe astratta ComponenteAstronave COMPONENT
class ComponenteAstronave(ABC):
    def __init__(self, nome):
        self.nome = nome
        
    @abstractmethod
    def operation(self):
        pass
    def add(self, componente):
        pass
    def remove(self, componente):
        pass
    def getChild(self, index):
        pass


# creo sottoclasse LEAF
class Sistema(ComponenteAstronave):
    def operation(self):
        print(f"Sistema {self.nome} in operazione.")
        
# creo sottoclasse COMPOSITE
class ModuloComplesso(ComponenteAstronave):
    def __init__(self, nome):
        super().__init__(nome)
        self._componenti = []
    def operation(self):
        print(f"Modulo Complesso -> {self.nome} in esecuzione:")
        for componente in self._componenti:
            componente.operation()
    def add(self, componente):
        self._componenti.append(componente)        
    def remove(self, componente):
        self._componenti.remove(componente)        
    def getChild(self, index):
        if index < 0 or index >= len(self._componenti):
            return None
        return self._componenti[index]
           

# creo istanze sistemi
sistema_navigazione = Sistema("Navigazione")
sistema_difesa = Sistema("Difesa")
sistema_ricerca = Sistema("Ricerca")

# creo istanze modulo
modulo_comando = ModuloComplesso("Modulo Comando")
# agginugo al modulo complesso i sistemi di navigazione e difesa
modulo_comando.add(sistema_navigazione)
modulo_comando.add(sistema_difesa)

# creo istanze modulo
modulo_scienza = ModuloComplesso("Modulo Scienza")
# agginugo al modulo complesso i sistemi di ricerca
modulo_scienza.add(sistema_ricerca)

# creo modulo principale astronave e aggiungo tutti i moduli creati
millenuimFalco = ModuloComplesso("MilleniumFalco")
millenuimFalco.add(modulo_comando)
millenuimFalco.add(modulo_scienza)

# stampo le operazioni
millenuimFalco.operation()