class No_Plaza_Disponible_Para_Abonar(Exception):
    def __init__(self):
        self.__mensaje = 'No hay plazas no abonadas libres de ese tipo de vehiculo que puedan ser abonadas.'

    @property
    def mensaje(self):
        return self.__mensaje
    @mensaje.setter
    def mensaje(self,mensaje):
        self.__mensaje = mensaje
