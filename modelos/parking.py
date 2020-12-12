class Parking:
    def __init__(self,nombre, plazas):
        self.__nombre = nombre
        self.__plazas = plazas

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


