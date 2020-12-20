class No_Caduca_Abonos_Este_Mes(Exception):
    def __init__(self):
        self.__mensaje = 'Este mes no caduca ningún abono.'

    @property
    def mensaje(self):
        return self.__mensaje
    @mensaje.setter
    def mensaje(self,mensaje):
        self.__mensaje = mensaje
