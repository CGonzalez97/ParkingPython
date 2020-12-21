class No_Hay_Abonos_Vigentes(Exception):
    def __init__(self):
        self.__mensaje = 'No hay abonos vigentes.'

    @property
    def mensaje(self):
        return self.__mensaje
    @mensaje.setter
    def mensaje(self,mensaje):
        self.__mensaje = mensaje
