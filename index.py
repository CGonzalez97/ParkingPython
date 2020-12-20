import threading
#from datetime import time
import time

from modelos.abono import Abono
from modelos.cliente import Cliente
from modelos.cobro import Cobro
from modelos.parking import Parking
from modelos.plaza import Plaza
from modelos.ticket import Ticket
from modelos.vehiculo import Vehiculo, Coche, Moto, Vehiculo_pmr
from repositorios.abono_repositorio import Abono_Repositorio
from repositorios.cobro_repositorio import Cobro_Repositorio
from repositorios.ticket_repositorio import Ticket_Repositorio
from servicios.cliente_servicio import Cliente_Servicio
from servicios.parking_servicio import Parking_Servicio
from vistas.vista_parking import Vista_Parking
from vistas.vista_cliente import Vista_Cliente
from vistas.vista_general import Vista_General
import math
from excepciones.Matricula_Erronea import Matricula_Erronea
from excepciones.Plaza_no_encontrada import Plaza_no_encontrada
from excepciones.No_Ticket import No_Ticket
from excepciones.Pin_Erroneo import Pin_Erroneo
from excepciones.No_Abono_Especificado import No_Abono_Especificado
from excepciones.No_Plaza_Abono_Especificado import No_Plaza_Abono_Especificado
from excepciones.No_Plaza_Abonada_Ocupada_Con_Dni_Especificado import No_Plaza_Abonada_Ocupada_Con_Dni_Especificado
from excepciones.No_Cobros import No_Cobros
from excepciones.No_Cobros_Periodo_Especificado import No_Cobros_Periodo_Especificado
from excepciones.No_Abonos_Anuales import No_Abonos_Anuales
from excepciones.No_Hay_Abonos import No_Hay_Abonos
from excepciones.Tipo_Vehiculo_Inexistente import Tipo_Vehiculo_Inexistente
from excepciones.No_Plaza_Libre_Para_Abonar import No_Plaza_Disponible_Para_Abonar
from excepciones.No_Caducan_Abonos_Este_Mes import No_Caduca_Abonos_Este_Mes
from excepciones.No_Caducan_Abonos_En_Diez_Dias import No_Caducan_Abonos_En_Diez_Dias
from excepciones.No_Hay_Abonos_Vigentes import No_Hay_Abonos_Vigentes

#Instanciacion repositorios
ticket_repositorio = Ticket_Repositorio()
cobro_repositorio = Cobro_Repositorio()
abono_repositorio = Abono_Repositorio()

#Instanciacion servicios
cliente_servicio = Cliente_Servicio()
parking_servicio = Parking_Servicio()

#Instanciacion vistas
vista_parking = Vista_Parking()
vista_cliente = Vista_Cliente()
vista_general = Vista_General()

no_plazas = False
cargar = input('Desea usar datosde la sesión anterior.(S/N)').upper()
if(cargar == 'S'):
    try:
        ticket_repositorio.cargar()
    except EOFError:
        print('No hay tickets en DB.')
    try:
            abono_repositorio.cargar()
    except EOFError:
        print('No hay abonos en DB.')
    try:
        cobro_repositorio.cargar()
    except EOFError:
        print('No hay cobros en DB.')
    try:
        parking = Parking('Parking centro',[])
        parking.cargar()
    except EOFError:
        print('No hay plazas en DB.')
        no_plazas = True

if(cargar == 'N' or no_plazas):
    #Calculo del numero de plazas de cda tipo
    n_plazas_totales = int(input('¿Cuántas plazas tendrá el parking?'))
    n_plazas_coche = math.ceil(n_plazas_totales / 100 * 70)
    n_plazas_moto = math.floor(n_plazas_totales / 100 * 15)
    n_plazas_pmr = math.floor(n_plazas_totales / 100 * 15)
    print('Plazas coche',n_plazas_coche)
    print('Plazas moto',n_plazas_moto)
    print('Plazas pmr',n_plazas_pmr)

    #Creo el array de plazas
    plazas = []
    for i in range(0,n_plazas_coche):
        plazas.append(Plaza(i,False,False,'coche'))
    for i in range(0,n_plazas_moto):
        plazas.append(Plaza((i+n_plazas_coche),False,False,'moto'))
    for i in range(0,n_plazas_pmr):
        plazas.append(Plaza((i+n_plazas_coche+n_plazas_moto),False,False,'pmr'))

    #Instancio el parking y le anyado el array de plazas
    parking = Parking('Parking centro',plazas)
    parking.guardar()


# for i in parking.plazas:
#     print(i.tipo)

print(parking_servicio.informar_plazas(parking.plazas))
print('-'*50)

#global acabar_programa


def correr_programa():
    salir = False
    # salir_submenu_cliente = False
    # salir_submenu_parking = False
    # salir_submenu_abonos = False
    #opcion = None
    while not salir:
        opcion = int(input(vista_general.preguntar_tipo_usuario()))
        if(opcion == 1):
            #Menu gestor
            salir_submenu_parking = False
            print('-'*50)
            print(vista_parking.introducir_a_menu_gestor())
            while not salir_submenu_parking:
                opcion = int(input(vista_parking.mostrarOpcionesParkin()))
                if(opcion == 1):
                    print('-'*50)
                    #print('Estado parking')
                    print(parking_servicio.informar_plazas(parking.plazas))
                    print('-'*50)
                elif(opcion == 2):
                    #print('Facturación')
                    print('-'*50)
                    #print(parking_servicio.facturar(vista_parking, cobro_repositorio),'€')
                    try:
                        print("{0:.2f}€".format(parking_servicio.facturar(vista_parking, cobro_repositorio)))
                    except (No_Cobros, No_Cobros_Periodo_Especificado) as error:
                        print(error.mensaje)
                    print('-'*50)
                elif(opcion == 3):
                    print('-'*50)
                    print('Consulta de abonados')
                    try:
                        parking_servicio.consultar_abonados(abono_repositorio.lista_abonos)
                    except No_Abonos_Anuales as error:
                        print(error.mensaje)
                    print('-'*50)
                elif(opcion == 4):
                    salir_submenu_abonos = False
                    print('-'*50)
                    print('Menu abonos')
                    while not salir_submenu_abonos:
                        opcion = int(input(vista_parking.mostrarMenuAbonos()))
                        if(opcion == 1):
                            #print('Mostrar abonos')
                            print('-'*50)
                            try:
                                parking_servicio.mostrar_abonos(abono_repositorio.lista_abonos)
                            except No_Hay_Abonos as  error:
                                print(error.mensaje)
                            print('-'*50)
                        elif(opcion == 2):
                            print('-'*50)
                            print('Dar alta a un abono')
                            try:
                                parking_servicio.dar_alta_abono(parking, vista_parking, abono_repositorio)
                            except (No_Plaza_Disponible_Para_Abonar, Tipo_Vehiculo_Inexistente) as error:
                                print(error.mensaje)
                            parking.guardar()
                            print('-'*50)
                        elif(opcion == 3):
                            print('-'*50)
                            print('Modificar abono')
                            dni_abono_a_modificar = input(vista_parking.pedir_matricula_abono_actualizar())
                            opcion_modificar = int(input(vista_parking.introducir_modificar_abono()))
                            if(opcion_modificar == 1):
                                nombre_nuevo = input(vista_parking.introducir_nombre_modificar())
                                dni_nuevo = input(vista_parking.introducir_dni_modificar())
                                matricula_nueva = input(vista_parking.introducir_matricula_modificar())
                                try:
                                    parking_servicio.modificar_abono(dni_abono_a_modificar,nombre_nuevo, dni_nuevo, matricula_nueva, abono_repositorio)
                                except No_Abono_Especificado as error:
                                    print(error.mensaje)
                            elif(opcion_modificar == 2):
                                try:
                                    parking_servicio.renovar_abono(abono_repositorio,dni_abono_a_modificar)
                                except No_Abono_Especificado as error:
                                    print(error.mensaje)
                            print('-'*50)
                        elif(opcion == 4):
                            print('-'*50)
                            print('Eliminar abono')
                            dni_eliminacion = input(vista_parking.pedir_matricula_abono_eliminar())
                            try:
                                parking_servicio.eliminar_datos_abonado(dni_eliminacion,abono_repositorio)
                            except No_Abono_Especificado as error:
                                print(error.mensaje)
                            print('-'*50)
                        elif(opcion == 5):
                            #print('Mostrar caducan este mes')
                            print('-'*50)
                            try:
                                parking_servicio.mostrar_abonos_caducan_mes(abono_repositorio.lista_abonos,vista_parking)
                            except No_Caduca_Abonos_Este_Mes as error:
                                print(error.mensaje)
                            print('-'*50)
                        elif(opcion == 6):
                            #print('Mostrar caducan diez días')
                            print('-'*50)
                            try:
                                parking_servicio.mostrar_abonos_caducan_diez(abono_repositorio.lista_abonos,vista_parking)
                            except No_Caducan_Abonos_En_Diez_Dias as error:
                                print(error.mensaje)
                            print('-'*50)
                        elif(opcion == 7):
                            print('-'*50)
                            print('Total abonos anuales')
                            try:
                                parking_servicio.calcular_anuales(abono_repositorio)
                            except No_Hay_Abonos_Vigentes as error:
                                print(error.mensaje)
                            print('-'*50)
                        elif(opcion == 0):
                            print('-'*50)
                            print('Salir submenu abonos')
                            salir_submenu_abonos = True
                elif(opcion == 0):
                    print('-'*50)
                    print('Salir menu parking')
                    salir_submenu_parking = True
        elif(opcion == 2):
            #Menu cliente
            salir_submenu_cliente = False
            opcion = int(input(vista_cliente.preguntarOpcionCliente()))
            if(opcion == 1):
                print('-'*50)
                print('Depositar vehiculo')
                tipo_v = input(vista_cliente.pedirTipoVehiculoDepositar())
                matricula = input(vista_cliente.pedirMatriculaDepositar())
                vehiculo = None
                if(tipo_v == 'coche'):
                    vehiculo = Coche(matricula)
                elif(tipo_v == 'moto'):
                    vehiculo = Moto(matricula)
                elif(tipo_v == 'pmr'):
                    vehiculo = Vehiculo_pmr(matricula)
                try:
                    cliente_servicio.depositarVehiculo(vehiculo, parking, vista_cliente, ticket_repositorio)
                except Plaza_no_encontrada as error:
                    print(error.mensaje)
                parking.guardar()
                print('-'*50)
            elif(opcion == 2):
                print('-'*50)
                print('Retirar vehiculo')
                matricula = input(vista_cliente.pedirMatriculaRetirarVehiculo())
                pin = int(input(vista_cliente.pedirPinRetirarVehiculo()))
                try:
                    cliente_servicio.retirarVehiculo(matricula,pin,ticket_repositorio,
                                                 vista_cliente,parking,cobro_repositorio)
                except (Pin_Erroneo, Matricula_Erronea, No_Ticket, Plaza_no_encontrada) as error:
                    print(error.mensaje)
                parking.guardar()
                print('-'*50)
            elif(opcion == 3):
                print('-'*50)
                print('Depositar abonados')
                dni = input(vista_cliente.pedirDni())
                matricula = input(vista_cliente.pedirMatricula())
                try:
                    cliente_servicio.depositar_abonado(dni, matricula,parking,abono_repositorio)
                except (No_Plaza_Abono_Especificado, No_Abono_Especificado) as error:
                    print(error.mensaje)
                parking.guardar()
                print('-'*50)
            elif(opcion == 4):
                print('-'*50)
                print('Retirar abonado')
                dni = input(vista_cliente.pedirDni())
                try:
                    cliente_servicio.retirar_abonado(dni,parking,abono_repositorio)
                except No_Plaza_Abonada_Ocupada_Con_Dni_Especificado as error:
                    print(error.mensaje)
                parking.guardar()
                print('-'*50)
            elif(opcion == 0):
                print('-'*50)
                print('Salir menu cliente')
                salir_submenu_cliente = True
        elif(opcion == 0):
            print('Saliendo, espere por favor')
            salir = True
#correr_programa()

def guardar_concurrente():
    acabar_programa = False
    n_inicial_hilos = len(threading.enumerate())
    while not acabar_programa:
        if(len(threading.enumerate()) < n_inicial_hilos):
            acabar_programa = True
        ticket_repositorio.guardar()
        abono_repositorio.guardar()
        cobro_repositorio.guardar()
        parking.guardar()
        time.sleep(5)#Guardado general cada 30 segundos


hilo_1 = threading.Thread(target=correr_programa)
#hilo_1.daemon = True
hilo_2 = threading.Thread(target=guardar_concurrente)
#hilo_2.daemon = True
#threads = [threading.Thread(target=correr_programa), threading.Thread(target=guardar_concurrente)]
threads = [hilo_1, hilo_2]
[thread.start() for thread in threads]
[thread.join() for thread in threads]





