class No_Abonos_Anuales(Exception):
    def __init__(self):
        self.__mensaje = 'No hay abonos anuales.'

    @property
    def mensaje(self):
        return self.__mensaje
    @mensaje.setter
    def mensaje(self,mensaje):
        self.__mensaje = mensaje
