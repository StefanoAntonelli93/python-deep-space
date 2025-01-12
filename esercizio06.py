# observer
"""
- subject(abstrat subject)
- observer(abstract observer)
- sistema di allarme(concrete subject)
- ponte di comando, sala motori, cabine equipaggio(concrete observers)

"""

# importo metodo per abstract class
from abc import ABC, abstractmethod

# creo classe astratta observer
class Observer(ABC):
    @abstractmethod
    def aggiorna(self, status: bool):
        pass
    
#  creo classe astratta subject
class Subject(ABC):
    def __init__(self):
        self._observers = [] 
    def aggiungi_observer(self, observer: Observer):
        self._observers.append(observer)
    def rimuovi_observer(self, observer: Observer):
        self._observers.remove(observer)
    def notifica_observers(self, status: bool):
        for observer in self._observers:
            observer.aggiorna(status)             
            
# creo sottoclasse di subject, SistemaDiAllarme(concrete subject)
class SistemaDiAllarme(Subject):
    def __init__(self):
        # invoco inizializzatore superclasse
        super().__init__()
        self._is_active = False
    def attiva_allarme(self):
        self._is_active = True
        self.notifica_observers(self._is_active)
    def disattiva_allarme(self):
        self._is_active = False
        self.notifica_observers(self._is_active)
        
# creo sottoclasse di observer, PonteDiComando(concrete observer)
class PonteDiComando(Observer):
    def aggiorna(self, status:bool):
        if status == True:
            print("Ponte di Comando: Blocco tutte le entrate e le uscite!")
        else:
            print("Ponte di Comando: Riapro entrate e uscite!")    
            
# creo sottoclasse SalaMotori            
class SalaMotori(Observer):
    def aggiorna(self, status:bool):
        if status == True:
            print("Sala Motori: Preparo manovra evasiva!")
        else:
            print("Sala Motori:Ripresa delle normali attività!")     
    
# creo sottoclasse CabineEquipaggio
class CabineEquipaggio(Observer):
    def aggiorna(self, status:bool):
        if status == True:
            print("Cabine Equipaggio: Tutti all'interno delle cabine in sicurezza!")
        else:
            print("Cabine Equipaggio: Tutto ok, è possibile uscire dalle cabine!")    
      

# simulazione allarme
if __name__ == "__main__":
    allarme = SistemaDiAllarme()
    ponte_comando = PonteDiComando()
    motori = SalaMotori()
    cabine = CabineEquipaggio()
    
    allarme.aggiungi_observer(ponte_comando)
    allarme.aggiungi_observer(motori)
    allarme.aggiungi_observer(cabine)
    
    print("\nSimulazione primo allarme:")
    allarme.attiva_allarme()
    print("\nFine primo allarme:")
    allarme.disattiva_allarme()
    
    # rimuovi allerme sul ponte di comando
    allarme.rimuovi_observer(ponte_comando)
    print("\nSimulazione secondo allarme:")
    allarme.attiva_allarme()
    print("\nFine secondo allarme:")
    allarme.disattiva_allarme()
    