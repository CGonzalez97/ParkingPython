class Cobro_Repositorio:
    def __init__(self):
        self.__lista_cobros = []

    @property
    def lista_cobros(self):
        return self.__lista_cobros
    @lista_cobros.setter
    def lista_cobros(self, lista):
        self.__lista_cobros = lista
