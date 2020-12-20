class No_Abono_Especificado(Exception):
    def __init__(self):
        self.__mensaje = 'No hay abono con esos datos'

    @property
    def mensaje(self):
        return self.__mensaje
    @mensaje.setter
    def mensaje(self,mensaje):
        self.__mensaje = mensaje
