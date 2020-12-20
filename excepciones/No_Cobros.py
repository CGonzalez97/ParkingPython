class No_Cobros(Exception):
    def __init__(self):
        self.__mensaje = 'No hay cobros sin abono realizados.'

    @property
    def mensaje(self):
        return self.__mensaje
    @mensaje.setter
    def mensaje(self,mensaje):
        self.__mensaje = mensaje
