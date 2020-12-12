from random import randint

class Ticket:
    def __init__(self, vehiculo, plaza, fechaDeposito):
        self.__vehiculo = vehiculo
        self.__plaza = plaza
        self.__fecha_deposito = fechaDeposito
        self.__pin = self.generar_pin()

    @property
    def vehiculo(self):
        return self.__vehiculo
    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    @property
    def plaza(self):
        return self.__plaza
    @plaza.setter
    def plaza(self, plaza):
        self.__plaza = plaza

    @property
    def fechaDeposito(self):
        return self.__fechaDeposito
    @fechaDeposito.setter
    def fechaDeposito(self, fechaDeposito):
        self.__fechaDeposito = fechaDeposito

    @property
    def pin(self):
        return self.__pin
    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    def generar_pin(self):
        return randint(0,999999)
