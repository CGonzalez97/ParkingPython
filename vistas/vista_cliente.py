class Vista_Cliente():
    def __init__(self):
        pass

    def preguntarOpcionCliente(self):
        return '¿Qué opción desea?' \
               '\n1.Depositar coche.' \
               '\n2.Retirar vehiculo.' \
               '\n3.Depositar con abono.' \
               '\n4.Retirar con abono.' \
               '\n0.Salir.'

    def pedirMatriculaDepositar(self):
        return 'Inserte la matrícula de su vehículo.'

    def pedirTipoVehiculoDepositar(self):
        return 'Inserte el tipo de vehiculo, coche, moto, vehiculo_pmr.'


    def pedirMatriculaRetirarVehiculo(self):
        return 'Inserte la matrícula del vehículo a retirar.'

    def pedirPinRetirarVehiculo(self):
        return 'Inserte el pin.'

    def indicarMatriculaNoEncontrada(self):
        return 'La matrícula que indicó no se encuentra en la base de datos.'

    def indicarPinErroneo(self):
        return 'Introduzca un pin válido.'

    def confirmarRetiradaDeVehiculo(self):
        return 'Pase a recoger su vehículo.\nPD:el rayón ya estaba.'

    def indicarNoHayTickets(self):
        return 'No hay ningun ticket en la base de datos.'

    def plazaEncontrada(self):
        return 'Se ha encontrado una plaza disponible para su vehículo.'

    def plazaNoEncontrada(self):
        return'No hay plazas disponibles actualmente.'


    def pedirMatricula(self):
        return 'Introduzca su matrícula.'

    def pedirDni(self):
        return 'Introduzca su dni.'
