#  FACTORY METHOD

# creo classe ModuloSpaziale - PRODUCT -
class ModuloSpaziale:
    def __init__(self, nome, tipo, funzione):
        self.nome = nome
        self.tipo = tipo
        self.funzione = funzione
        
#  creo sottoclassi moduli - CONCRETE PRODUCTS -
class ModuloEsplorazione(ModuloSpaziale):
    def __init__(self):
        super().__init__("Modulo Esplorazione","Esplorazione","Esplorare nuovi settori spaziali")       

class ModuloDifesa(ModuloSpaziale):
    def __init__(self):
        super().__init__("Modulo Difesa","Difesa","Proteggere l'astronave da nuove minacce")       

class ModuloRicerca(ModuloSpaziale):
    def __init__(self):
        super().__init__("Modulo Ricerca","Ricerca","Condurre ricerche scientifiche")       

class ModuloSupportoVitale(ModuloSpaziale):
    def __init__(self):
        super().__init__("Modulo Supporto Vitale","Supporto Vitale","Fornire approvvigionamenti all'equipaggio")       
        
        
# creo classe astratta Creator - CREATOR -        
from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    # factoryMethod()
    def crea_modulo(self, tipo_modulo):
        pass
    
# creo sottoclasse factory modulo spaziale- CONCRETE CREATOR -  

class FactoryModuliSpaziali(Creator):
    def crea_modulo(self, tipo_modulo):
        if tipo_modulo == "Esplorazione":
            return ModuloEsplorazione()
        elif tipo_modulo == "Difesa":
            return ModuloDifesa()
        elif tipo_modulo == "Ricerca":
            return ModuloRicerca()
        elif tipo_modulo == "Supporto Vitale":
            return ModuloSupportoVitale()
        else:
            raise ValueError(f"Tipo di modulo non valido: {tipo_modulo}")
       

# Test della Factory
factory = FactoryModuliSpaziali()

modulo_esplorazione = factory.crea_modulo("Esplorazione")
print(f"Modulo creato: {modulo_esplorazione.nome}")

modulo_difesa = factory.crea_modulo("Difesa")
print(f"Modulo creato: {modulo_difesa.nome}")

modulo_ricerca = factory.crea_modulo("Ricerca")
print(f"Modulo creato: {modulo_ricerca.nome}")

try:
  factory.crea_modulo("Sterminio degli innocenti")
except ValueError as e:
  print(f"Errore: {e}")
