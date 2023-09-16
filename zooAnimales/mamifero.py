from animal import Animal


class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)
        pass

    def getPelaje(self):
        return self._pelaje
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    def getPatas(self):
        return self._patas
    def setPatas(self, patas):
        self._patas = patas
