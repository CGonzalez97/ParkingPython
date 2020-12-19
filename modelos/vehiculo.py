class Vehiculo:
    def __init__(self, matricula):
        self.__matricula = matricula
        self.__tarifa = 0

    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
    @property
    def tarifa(self):
        return self.__tarifa
    @tarifa.setter
    def tarifa(self, tarifa):
        self.__tarifa = tarifa

class Coche(Vehiculo):
    def __init__(self, matricula):
        super().__init__(matricula)
        self.__tarifa = 0.12

class Moto(Vehiculo):
    def __init__(self, matricula):
        super().__init__(matricula)
        self.__tarifa = 0.08

class Vehiculo_pmr(Vehiculo):#Vehiculo de persona de movilidad reducida
    def __init__(self, matricula):
        super().__init__(matricula)
        self.__tarifa = 0.1
