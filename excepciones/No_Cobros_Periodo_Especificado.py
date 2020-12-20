class No_Cobros_Periodo_Especificado(Exception):
    def __init__(self):
        self.__mensaje = 'No hay cobros efectuados en el periodo indicado.'

    @property
    def mensaje(self):
        return self.__mensaje
    @mensaje.setter
    def mensaje(self,mensaje):
        self.__mensaje = mensaje
