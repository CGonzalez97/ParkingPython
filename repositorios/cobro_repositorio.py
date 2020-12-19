import pickle

class Cobro_Repositorio:
    def __init__(self):
        self.__lista_cobros = []
        self.__directorio = '../persistencia/cobros.pckl'

    @property
    def lista_cobros(self):
        return self.__lista_cobros
    @lista_cobros.setter
    def lista_cobros(self, lista):
        self.__lista_cobros = lista
    @property
    def directorio(self):
        return self.__directorio
    @directorio.setter
    def directorio(self, directorio):
        self.__directorio = directorio

    def guardar(self):
        fichero = open(self.directorio,'wb')
        pickle.dump(self.lista_cobros,fichero)
        fichero.close()

