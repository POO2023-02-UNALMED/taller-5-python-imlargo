from animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)
    
    def getcolorPiel(self):
        return self._colorPiel
    def setcolorPiel(self, colorPiel):
        self._colorPiel = colorPiel
    def isVenenoso(self):
        return self._venenoso
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
        
    #----
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
        
    def movimiento(self):
        return "saltar"
    
    @classmethod
    def crearRana(cls, nombre, edad, genero, ):
        animal = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas += 1
        return animal
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero, ):
        animal = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.salamandras += 1
        return animal