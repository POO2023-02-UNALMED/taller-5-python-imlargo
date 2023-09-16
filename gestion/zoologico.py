from gestion.zona import Zona

class Zoologico:
    
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []
        pass
    
    
    def getNombre(self):
        return self._nombre
    def getUbicacion(self):
        return self._ubicacion
    def getZona(self):
        return self._zonas
    
    def cantidadTotalAnimales(self):
        i = 0
        for zona in self._zonas:
            i += zona.cantidadAnimales()
        return i 
    
    def agregarZonas(self, zona):
        self._zonas.append(zona)