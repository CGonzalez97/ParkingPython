import pickle

class Abono_Repositorio():
    def __init__(self):
        self.__lista_abonos = []
        self.__directorio = '../persistencia/abono.pckl'
        #self.__fichero = None

    @property
    def lista_abonos(self):
        return self.__lista_abonos
    @lista_abonos.setter
    def lista_abonos(self, lista):
        self.__lista_abonos = lista
    @property
    def directorio(self):
        return self.__directorio
    @directorio.setter
    def directorio(self, directorio):
        self.__directorio = directorio

    def guardar(self):
        fichero = open(self.directorio,'wb')
        pickle.dump(self.lista_abonos,fichero)
        fichero.close()
