import pickle

class Parking:
    def __init__(self,nombre, plazas):
        self.__nombre = nombre
        self.__plazas = plazas
        self.__directorio = './persistencia/plazas.pckl'

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def plazas(self):
        return self.__plazas
    @plazas.setter
    def plazas(self, plazas):
        self.__plazas = plazas
    @property
    def directorio(self):
        return self.__directorio
    @directorio.setter
    def directorio(self, directorio):
        self.__directorio = directorio

    def guardar(self):
        fichero = open(self.directorio,'wb')
        pickle.dump(self.plazas,fichero)
        fichero.close()
    def cargar(self):
        fichero = open(self.directorio,'rb')
        self.plazas = pickle.load(fichero)
        fichero.close()


