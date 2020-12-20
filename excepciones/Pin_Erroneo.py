class Pin_Erroneo(Exception):
    def __init__(self):
        self.__mensaje = 'El pin introducido no es válido.'

    @property
    def mensaje(self):
        return self.__mensaje
    @mensaje.setter
    def mensaje(self,mensaje):
        self.__mensaje = mensaje
