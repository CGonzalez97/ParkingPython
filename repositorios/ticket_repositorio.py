import pickle

class Ticket_Repositorio:
    def __init__(self):
        self.__lista_tickets = []
        self.__directorio = './persistencia/tickets.pckl'

    @property
    def lista_tickets(self):
        return self.__lista_tickets
    @lista_tickets.setter
    def lista_tickets(self, lista):
        self.__lista_tickets = lista
    @property
    def directorio(self):
        return self.__directorio
    @directorio.setter
    def directorio(self, directorio):
        self.__directorio = directorio

    def guardar(self):
        fichero = open(self.directorio,'wb')
        pickle.dump(self.lista_tickets,fichero)
        fichero.close()

    def cargar(self):
        fichero = open(self.directorio,'rb')
        self.lista_tickets = pickle.load(fichero)
        fichero.close()


