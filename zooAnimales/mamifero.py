from animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0
    
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        Animal.__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)
        pass