from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
    
    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas

    #----
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
        
    def movimiento(self):
        return "volar"
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        animal = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        cls.halcones += 1
        return animal
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        animal = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        cls.aguilas += 1
        return animal