class Zona:
    
    def __init__(self, nombre, zoo):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []
        pass
    
    #set y get...
    def getZoo(self):
        return self._zoo
    
    def getNombre(self):
        return self._nombre

    def setZoo(self, zoo):
        self._zoo = zoo
    
    def agregarAnimales(self, animal):
        self._animales.append(animal)
        animal.setZona(self)
        
    def cantidadAnimales(self):
        return len(self._animales)
    