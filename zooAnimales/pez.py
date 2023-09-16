from animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas 
        Pez._listado.append(self)
    
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    def getCantidadAletas(self):
        return self._cantidadAletas
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas

    #----
    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
        
    def movimiento(self):
        return "nadar"
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        animal = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        cls.salmones += 1
        return animal
    
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        animal = Pez(nombre, edad, "oceano", genero, "gris", 6)
        cls.bacalaos += 1
        return animal
