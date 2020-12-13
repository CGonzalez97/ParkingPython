class Abono_Repositorio:
    def __init__(self):
        self.__lista_abonos = []

    @property
    def lista_abonos(self):
        return self.__lista_abonos
    @lista_abonos.setter
    def lista_abonos(self, lista):
        self.__lista_abonos = lista
