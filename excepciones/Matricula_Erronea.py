class Matricula_Erronea(Exception):
    def __init__(self):
        self.__mensaje = 'La matrícula que indicó no se encuentra en la base de datos.'

    @property
    def mensaje(self):
        return self.__mensaje
    @mensaje.setter
    def mensaje(self,mensaje):
        self.__mensaje = mensaje
