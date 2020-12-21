class Cliente():
    def __init__(self,dni, nombre, nTarjeta, vehiculo):
        self.__dni = dni
        self.__nombre = nombre
        self.__ntarjeta = nTarjeta
        self.__vehiculo = vehiculo

    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def ntarjeta(self):
        return self.__ntarjeta
    @ntarjeta.setter
    def ntarjeta(self, ntarjeta):
        self.__ntarjeta = ntarjeta

    @property
    def vehiculo(self):
        return self.__vehiculo
    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo



