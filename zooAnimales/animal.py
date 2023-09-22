import zooAnimales

class Animal:
    _totalAnimales = 0
    
    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales += 1
        
    #Set y get
    def getNombre(self):
        return self._nombre
    def setNombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    def getEdad(self):
        return self._edad
    def setEdad(self, nueva_edad):
        self._edad = nueva_edad
    def getHabitat(self):
        return self._habitat
    def setHabitat(self, nuevo_habitat):
        self._habitat = nuevo_habitat
    def getGenero(self):
        return self._genero
    def setGenero(self, nuevo_genero):
        self._genero = nuevo_genero
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    #....
    def getZona(self):
        return self._zona
    def setGenero(self, zona):
        self._zona = zona
    
    #....
    def toString(self):
        if (self._zona != None):
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona.getNombre()}, en el {((self._zona).getZoo())}"
        else:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
    
    @classmethod
    def totalPorTipo(cls):
        return f"Mamiferos : {zooAnimales.mamifero.Mamifero.cantidadMamiferos()}\nAves : {zooAnimales.ave.Ave.cantidadAves()}\nReptiles : {zooAnimales.reptil.Reptil.cantidadReptiles()}\nPeces : {zooAnimales.pez.Pez.cantidadPeces()}\nAnfibios : {zooAnimales.anfibio.Anfibio.cantidadAnfibios()}"
    
    def movimiento(self):
        return "desplazarse"