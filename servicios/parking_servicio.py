from datetime import datetime
from datetime import timedelta
#pip install dateutil
#from dateutil.relativedelta import relativedelta
from modelos.cliente import Cliente
from modelos.vehiculo import Vehiculo, Coche, Moto, Vehiculo_pmr
from modelos.abono import Abono


class Parking_Servicio:
    def __init__(self):
        pass

    #---------------
    #METODOS
    #---------------

    #Método informar sobre plazas
    #-------------------------------------------------------------
    def informar_plazas(self, lista_p):
        #Variables plazas coche
        libres_c = 0
        ocupadas_c = 0
        abonadas_libres_c = 0
        abonadas_ocupadas_c = 0

        #Variables plazas moto
        libres_m = 0
        ocupadas_m = 0
        abonadas_libres_m = 0
        abonadas_ocupadas_m = 0

        #Variables plazas movilidad reducida
        libres_mr = 0
        ocupadas_mr = 0
        abonadas_libres_mr = 0
        abonadas_ocupadas_mr = 0

        contador = 0
        for plaza in lista_p:
            if(plaza.tipo == 'coche'):
                if(plaza.abonada):
                    if(plaza.ocupada):
                        abonadas_ocupadas_c += 1
                    else:
                        abonadas_libres_c += 1
                else:
                    if(plaza.ocupada):
                        ocupadas_c += 1
                    else:
                        libres_c += 1
            elif(plaza.tipo == 'moto'):
                if(plaza.abonada):
                    if(plaza.ocupada):
                        abonadas_ocupadas_m += 1
                    else:
                        abonadas_libres_m += 1
                else:
                    if(plaza.ocupada):
                        ocupadas_m += 1
                    else:
                        libres_m += 1
            elif(plaza.tipo == 'pmr'):
                if(plaza.abonada):
                    if(plaza.ocupada):
                        abonadas_ocupadas_mr += 1
                    else:
                        abonadas_libres_mr += 1
                else:
                    if(plaza.ocupada):
                        ocupadas_mr += 1
                    else:
                        libres_mr += 1


        lista_claves = ['libres_coche',
                            'ocupadas_coche',
                            'abonadas_libres_coche',
                            'abonadas_ocupadas_coche',
                            'libres_moto',
                            'ocupadas_moto',
                            'abonadas_libres_moto',
                            'abonadas_ocupadas_moto',
                            'libres_movilidad_reducida',
                            'ocupadas_movilidad_reducida',
                            'abonadas_libres_movilidad_reducida',
                            'abonadas_ocupadas_movilidad_reducida']

        lista_valores = [libres_c,
                             ocupadas_c,
                             abonadas_libres_c,
                             abonadas_ocupadas_c,
                             libres_m,
                             ocupadas_m,
                             abonadas_libres_m,
                             abonadas_ocupadas_m,
                             libres_mr,
                             ocupadas_mr,
                             abonadas_libres_mr,
                             abonadas_ocupadas_mr]

        return dict(zip(lista_claves, lista_valores))

    #-------------------------------------------------------------

    #FACTURAR

    def  facturar(self,vista_parking, cobro_repositorio):
        cuantia = 0
        if(len(cobro_repositorio.lista_cobros) <= 0):
            print('No hay cobros')
        fecha_inicial = datetime(int(input(vista_parking.pedirAnyoInicial())),#anyo
                                 int(input(vista_parking.pedirMesInicial())),#mes,
                                 int(input(vista_parking.pedirDiaInicial())),#dias,
                                 int(input(vista_parking.pedirHoraInicial())),#horas,
                                 int(input(vista_parking.pedirMinutosInicial())),#minutos
                                 0,0)#segundos y milisegundos
        fecha_final = datetime(int(input(vista_parking.pedirAnyoFinal())),#anyo
                                 int(input(vista_parking.pedirMesFinal())),#mes,
                                 int(input(vista_parking.pedirDiaFinal())),#dias,
                                 int(input(vista_parking.pedirHoraFinal())),#horas,
                                 int(input(vista_parking.pedirMinutosFinal())),#minutos
                                 0,0)#segundos y milisegundos
        for i in cobro_repositorio.lista_cobros:
            print('Cobro:',i.cobro_final, i.fecha_salida)
            if(i.fecha_salida > fecha_inicial
            and i.fecha_salida < fecha_final):
                cuantia += i.cobro_final

        return cuantia

    #---------------------------------------------------------

    #ABONOS

    #Crear fecha cancelacion
    #use_date = use_date+relativedelta(months=+1) <- ¿usar?
    def crear_fecha_cancelacion(self,fecha_ini, plazo):
        dias_mes = 30
        if(plazo == 'mensual'):
            return fecha_ini + timedelta(days=dias_mes)
        elif(plazo == 'trimestral'):
            return fecha_ini + timedelta(days=(dias_mes+3))
        elif(plazo == 'semestral'):
            return fecha_ini + timedelta(days=(dias_mes+6))
        elif(plazo == 'anual'):
            return fecha_ini + timedelta(days=(dias_mes+12))

    def facturacion_abono_concreto(self,
                                   plazo):
        if(plazo == 'mensual'):
            return 25
        elif(plazo == 'trimestral'):
            return 70
        elif(plazo == 'semestral'):
            return 130
        elif(plazo == 'anual'):
            return 200

    def dar_alta_abono(self,parking,
                       vista_parkin,
                       abono_repositorio):
        tipo_v = input(vista_parkin.pedirTipoVehiculoDepositar())
        lista_plazas = self.informar_plazas(parking.plazas)
        plaza_encontrada = False
        if(tipo_v == 'coche'):
            if(lista_plazas.get('libres_coche') > 0):
                plaza_encontrada = True
        elif(tipo_v == 'moto'):
            if(lista_plazas.get('libres_moto') > 0):
                plaza_encontrada = True
        elif(tipo_v == 'pmr'):#puede haver conflicto con el string vehiculo_pmr
            if(lista_plazas.get('libres_movilidad_reducida') > 0):
                plaza_encontrada = True

        if(plaza_encontrada):
            auxiliar_borrar_libre = False
            plazo = input(vista_parkin.pedirPlazo())
            matricula = input(vista_parkin.pedirMatricula())
            fecha_ini = datetime.now()
            fecha_can = self.crear_fecha_cancelacion(fecha_ini, plazo)
            facturacion = self.facturacion_abono_concreto(plazo)
            vehiculo_abonado = None
            if(tipo_v == 'coche'):
                vehiculo_abonado = Coche(matricula)
            elif(tipo_v == 'moto'):
                vehiculo_abonado = Moto(matricula)
            elif(tipo_v == 'pmr'):#puede haver conflicto con el string vehiculo_pmr
                vehiculo_abonado = Vehiculo_pmr(matricula)
            dni = input(vista_parkin.pedirDni())
            nombre = input(vista_parkin.pedirNombre())
            n_tarjeta = input(vista_parkin.pedirNTarjeta())
            cliente_a_abonar = Cliente(dni,nombre,n_tarjeta,vehiculo_abonado)
            abono_repositorio.lista_abonos.append(Abono(
                plazo, fecha_ini, fecha_can, facturacion, cliente_a_abonar
            ))

            for i in parking.plazas:
                if(not auxiliar_borrar_libre and
                not i.ocupada and not i.abonada and
                i.tipo == tipo_v):
                    i.abonada = True
                    auxiliar_borrar_libre = True

    def  mostrar_abonos(self, lista_abonos):
        for i in lista_abonos:
            print(i.mostrar())

    def mostrar_abonos_caducan_mes(self, lista_abonos,
                                   vista_parking):
        vista_parking.mostrarMensajesAbonoasACaducarEsteMes()
        ninguno = True
        for i in lista_abonos:
            if(i.fecha_cancelacion.year == datetime.now().year and
            i.fecha_cancelacion.month == datetime.now().month):
                print('-'*50)
                print(i.mostrar())
                print('-'*50)
                if(ninguno):
                    ninguno = False
        if(ninguno):
            print(vista_parking.mostrarSinCAducidadEsteMes())

    def mostrar_abonos_caducan_diez(self,lista_abonos,vista_parking):
        vista_parking.mostrarMensajesAbonoasACaducarDiezDias()
        ninguno = True
        for i in lista_abonos:
            if(i.fecha_cancelacion >= datetime.now() and
            i.fecha_cancelacion < (datetime.now() + timedelta(days=10))):
                print('-'*50)
                print(i.mostrar())
                print('-'*50)
                if(ninguno):
                    ninguno = False
        if(ninguno):
            print(vista_parking.mostrarSinCAducidadCercana())

    def calcular_anuales(self, abono_repositorio):
        contador = 0
        cuantia = 0
        for i in abono_repositorio.lista_abonos:
            if(i.fecha_cancelacion > datetime.now() and
            i.plazo == 'anual'):
                contador += 1
                cuantia += 200
        if(contador > 0):
            print(f'Hay en vigor {contador} abonos anuales,'
                  f'sumando un total de {cuantia}€.')
        else:
            print('No hhay abonos anuales vigentes.')

    #Consultar abonados
    def consultar_abonados(self, lista_abonos):
        for i in lista_abonos:
            print(type(i))
            if(i.plazo == 'anual'):
                print('-'*50)
                print(i.mostrar())
                print('-'*50)

    #Eliminar abono
    def eliminar_datos_abonado(self, dni, lista_abonos):
        encontrado = False
        for i in lista_abonos:
            if(not encontrado and i.cliente.dni == dni):
                i.cliente.vehiculo.matricula = 'Matricula de cliente eliminado'
                i.cliente.dni = 'Dni de cliente eliminado'
                i.cliente.nombre = 'nombre de cliente eliminado'
                encontrado = True
                print('Eliminacion con éxito.')
        if(not encontrado):
            print('No hay ningun abonado con ese dni')

    def modificar_abono(self, dni, nombre_n, dni_n, matricula_n, lista_abonos):
        encontrado = False
        for i in lista_abonos:
            if(not encontrado and i.cliente.dni == dni):
                if(not dni_n == 'M'):
                    i.cliente.dni = dni_n
                if(not nombre_n == 'M'):
                    i.cliente.nombre = nombre_n
                if(not matricula_n == 'M'):
                    i.cliente.vehiculo.matricula = matricula_n
                encontrado = True
                print('Eliminacion con éxito.')
        if(not encontrado):
            print('No hay ningun abonado con ese dni')

    def renovar_abono(self, lista_abonos, dni):
        encontrado = False
        for i in lista_abonos:
            if(not encontrado and i.cliente.dni == dni):
                if(i.plazo == 'mensual'):
                    i.fecha_cancelacion += timedelta(days=30)
                elif(i.plazo == 'trimestral'):
                    i.fecha_cancelacion += timedelta(days=90)
                elif(i.plazo == 'semestral'):
                    i.fecha_cancelacion += timedelta(days=180)
                elif(i.plazo == 'anual'):
                    i.fecha_cancelacion += timedelta(days=360)
                encontrado = True
                print('Renovado con éxito.')








