class Ticket_Repositorio:
    def __init__(self):
        self.__lista_tickets = []

    @property
    def lista_tickets(self):
        return self.__lista_tickets
    @lista_tickets.setter
    def lista_tickets(self, lista):
        self.__lista_tickets = lista


