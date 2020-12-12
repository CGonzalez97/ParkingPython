class Cobro:
    def __init__(self,fechaSalida, cobroFinal, ticket):
        self.__fecha_salida = fechaSalida
        self.__cobro_final = cobroFinal
        self.__ticket = ticket

    @property
    def fecha_salida(self):
        return self.__fecha_salida
    @fecha_salida.setter
    def fecha_salida(self, fecha_salida):
        self.__fecha_salida = fecha_salida

    @property
    def cobro_final(self):
        return self.__cobro_final
    @cobro_final.setter
    def cobro_final(self, cobro_final):
        self.__cobro_final = cobro_final

    @property
    def ticket(self):
        return self.__ticket
    @ticket.setter
    def ticket(self, ticket):
        self.__ticket = ticket
