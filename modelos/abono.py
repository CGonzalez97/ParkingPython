class Abono:
    def __init__(self, plazo, fechaActivacion, fechaCancelacion, facturacion, cliente):
        self.__plazo = plazo
        self.__fecha_activacion = fechaActivacion
        self.__fecha_cancelacion = fechaCancelacion
        self.__facturacion = facturacion
        self.__cliente = cliente

    @property
    def plazo(self):
        return self.__plazo
    @plazo.setter
    def plazo(self, plazo):
        self.__plazo = plazo

    @property
    def fecha_activacion(self):
        return self.__fecha_activacion
    @fecha_activacion.setter
    def fecha_activacion(self, fecha_activacion):
        self.__fecha_activacion = fecha_activacion

    @property
    def fecha_cancelacion(self):
        return self.__fecha_cancelacion
    @fecha_cancelacion.setter
    def fecha_cancelacion(self, fecha_cancelacion):
        self.__fecha_cancelacion = fecha_cancelacion

    @property
    def facturacion(self):
        return self.__facturacion
    @facturacion.setter
    def facturacion(self, facturacion):
        self.__facturacion = facturacion

    @property
    def cliente(self):
        return self.__cliente
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    
