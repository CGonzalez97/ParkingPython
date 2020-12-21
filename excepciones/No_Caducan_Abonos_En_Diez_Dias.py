class No_Caducan_Abonos_En_Diez_Dias(Exception):
    def __init__(self):
        self.__mensaje = 'No hay abonos.'

    @property
    def mensaje(self):
        return self.__mensaje
    @mensaje.setter
    def mensaje(self,mensaje):
        self.__mensaje = mensaje
