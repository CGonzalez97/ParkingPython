class Plaza_no_encontrada(Exception):
    def __init__(self):
        self.__mensaje = 'No hay plazas disponibles actualmente.'

    @property
    def mensaje(self):
        return self.__mensaje
    @mensaje.setter
    def mensaje(self,mensaje):
        self.__mensaje = mensaje
