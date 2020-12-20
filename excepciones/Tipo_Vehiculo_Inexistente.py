class Tipo_Vehiculo_Inexistente(Exception):
    def __init__(self):
        self.__mensaje = 'No existe ese tipo de vehiculo en el sistema.'

    @property
    def mensaje(self):
        return self.__mensaje
    @mensaje.setter
    def mensaje(self,mensaje):
        self.__mensaje = mensaje
