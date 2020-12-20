class No_Plaza_Abono_Especificado(Exception):
    def __init__(self):
        self.__mensaje = 'No hay plaza que coincida con su abono'

    @property
    def mensaje(self):
        return self.__mensaje
    @mensaje.setter
    def mensaje(self,mensaje):
        self.__mensaje = mensaje
