class Plaza:
    def __init__(self,id, ocupada, abonada, tipo):
        self.__id = id
        self.__ocupada = ocupada
        self.__abonada = abonada
        self.__tipo = tipo

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def ocupada(self):
        return self.__ocupada
    @ocupada.setter
    def ocupada(self, ocupada):
        self.__ocupada = ocupada

    @property
    def abonada(self):
        return self.__abonada
    @abonada.setter
    def abonada(self, abonada):
        self.__abonada = abonada

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo



