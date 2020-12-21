class No_Ticket(Exception):
    def __init__(self):
        self.__mensaje = 'No hay ningun ticket en la base de datos.'

    @property
    def mensaje(self):
        return self.__mensaje
    @mensaje.setter
    def mensaje(self,mensaje):
        self.__mensaje = mensaje
