class No_Plaza_Abonada_Ocupada_Con_Dni_Especificado(Exception):
    def __init__(self):
        self.__mensaje = 'No hay plaza abonada ocupada con ese dni'

    @property
    def mensaje(self):
        return self.__mensaje
    @mensaje.setter
    def mensaje(self,mensaje):
        self.__mensaje = mensaje
