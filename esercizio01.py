# importo math cosi posso calcolare radice quadrata con i metodi python
import math

# creo classe Astronave

class Astronave():
    # inizializzatore
    def __init__(self, x, y):
        # name mangling attributi privati di difficile accesso al di fuori della classe stessa
        self.__x = x
        self.__y = y
    # Metodo per muovere l'astronave a una nuova posizione
    def muovi_a(self, dest_x, dest_y):
        self.__x = dest_x
        self.__y = dest_y
        print(f"Nuove Coordinate: {self.__x}, {self.__y}")

    # Metodo per calcolare la distanza euclidea
    def distanza_da(self, dest_x, dest_y):
        return math.sqrt((dest_x - self.__x) ** 2 + (dest_y - self.__y) ** 2) 
    

#  creo istanza astronave 

MilleniumFalco = Astronave(0, 0)
Rocket07 = Astronave(1, 2)

MilleniumFalco.muovi_a(5, 5)
Rocket07.muovi_a(6, 8)

distanza01 = MilleniumFalco.distanza_da(0, 0)
distanza02 = Rocket07.distanza_da(1, 2)

print(f"Il MilleniumFalco è a {distanza01} unità di distanza dalla precedente posizione!")
print(f"Il Rocket07 è a {distanza02} unità di distanza dalla precedente posizione!")