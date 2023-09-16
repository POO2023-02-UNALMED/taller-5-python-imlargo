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
        pass
    
    def getcolorPiel(self):
        return self._colorPiel
    def setcolorPiel(self, colorPiel):
        self._colorPiel = colorPiel
    def getVenenoso(self):
        return self._venenoso
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
        
    