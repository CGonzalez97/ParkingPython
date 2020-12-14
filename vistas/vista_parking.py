class Vista_Parking():
    def __init__(self):
        pass

    def mostrarOpcionesParkin(self):
        return '1.Estado del parkin.' \
               '\n2.Facturación.' \
               '\n3.Consulta de abonados.' \
               '\n4.Acceder al menú abonos.' \
               '\n0.Salir.'


    def informarValoresAIntroducir(self):
        return 'Necesitamos dos fechas.'

    def pedirAnyoInicial(self):
        return 'Introduzca el año de la fecha inicial.'

    def pedirMesInicial(self):
        return 'Introduzca el mes de la fecha inicial.'

    def pedirDiaInicial(self):
        return 'Introduzca el día de la fecha inicial.'

    def pedirHoraInicial(self):
        return 'Introduzca la hora de la fecha inicial.'

    def pedirMinutosInicial(self):
        return 'Introduzca los minutos de la fecha inicial.'

    def pedirAnyoFinal(self):
        return 'Introduzca el año de la fecha final.'

    def pedirMesFinal(self):
        return 'Introduzca el mes de la fecha final.'

    def pedirDiaFinal(self):
        return 'Introduzca el día de la fecha final.'

    def pedirHoraFinal(self):
        return 'Introduzca la hora de la fecha final.'

    def pedirMinutosFinal(self):
        return 'Introduzca los minutos de la fecha final.'


    #Abonos
    def mostrarMenuAbonos(self):
        return '1.Mostrar abonos.' \
               '\n2.Dar de alta un abono.'\
               '\n3.Modificar un abono.' \
               '\n4.Eliminar un abono.'\
               '\n5.Caducidad un mes.' \
               '\n6.Caducidad en diez dias.' \
               '\n7.Mostrar anuales.' \
               '\n0.Salir.'

    def pedirPlazo(self):
        return 'Indique el plazo:' \
               '\n-mensual' \
               '\n-trimestral' \
               '\n-semestral' \
               '\n-anual'

    def pedirDni(self):
        return 'Indique su dni.'

    def pedirNombre(self):
        return 'Indique su nombre y apellidos.'

    def pedirNTarjeta(self):
        return 'Indique su tarjeta de pago.'

    def pedirMatricula(self):
        return 'Inserte la matrícula de su vehículo.'

    def pedirTipoVehiculoDepositar(self):
        return 'Inserte el tipo de vehiculo, ' \
               'coche, ' \
               'moto, ' \
               'vehiculo_pmr'

    #Caducan este mes
    def mostrarMensajesAbonoasACaducarEsteMes(self):
        return 'Este mes caducan:'

    def mostrarSinCAducidadEsteMes(self):
        return 'No caduca ninguno este mes.'

    #Caducan en 10 dias
    def mostrarMensajesAbonoasACaducarDiezDias(self):
        return 'En diez dias caducan: '

    def mostrarSinCAducidadCercana(self):
        return 'No caduca ninguno próximamente.'


