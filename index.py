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

# for i in parking.plazas:
#     print(i.tipo)

print(parking_servicio.informar_plazas(parking.plazas))
print('-'*50)

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
                print("{0:.2f}€".format(parking_servicio.facturar(vista_parking, cobro_repositorio)))
                print('-'*50)
            elif(opcion == 3):
                print('-'*50)
                print('Consulta de abonados')
                parking_servicio.consultar_abonados(abono_repositorio.lista_abonos)
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
                        parking_servicio.mostrar_abonos(abono_repositorio.lista_abonos)
                        print('-'*50)
                    elif(opcion == 2):
                        print('-'*50)
                        print('Dar alta a un abono')
                        parking_servicio.dar_alta_abono(parking, vista_parking, abono_repositorio)
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
                            parking_servicio.modificar_abono(dni_abono_a_modificar,nombre_nuevo, dni_nuevo, matricula_nueva, abono_repositorio.lista_abonos)
                        elif(opcion_modificar == 2):
                            parking_servicio.renovar_abono(abono_repositorio.lista_abonos,dni_abono_a_modificar)
                        print('-'*50)
                    elif(opcion == 4):
                        print('-'*50)
                        print('Eliminar abono')
                        dni_eliminacion = input(vista_parking.pedir_matricula_abono_eliminar())
                        parking_servicio.eliminar_datos_abonado(dni_eliminacion,abono_repositorio.lista_abonos)
                        print('-'*50)
                    elif(opcion == 5):
                        #print('Mostrar caducan este mes')
                        print('-'*50)
                        parking_servicio.mostrar_abonos_caducan_mes(abono_repositorio.lista_abonos,vista_parking)
                        print('-'*50)
                    elif(opcion == 6):
                        #print('Mostrar caducan diez días')
                        print('-'*50)
                        parking_servicio.mostrar_abonos_caducan_diez(abono_repositorio.lista_abonos,vista_parking)
                        print('-'*50)
                    elif(opcion == 7):
                        print('-'*50)
                        print('Total abonos anuales')
                        parking_servicio.calcular_anuales(abono_repositorio)
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
            cliente_servicio.depositarVehiculo(vehiculo, parking, vista_cliente, ticket_repositorio)
            print('-'*50)
        elif(opcion == 2):
            print('-'*50)
            print('Retirar vehiculo')
            matricula = input(vista_cliente.pedirMatriculaRetirarVehiculo())
            pin = int(input(vista_cliente.pedirPinRetirarVehiculo()))
            cliente_servicio.retirarVehiculo(matricula,pin,ticket_repositorio,
                                             vista_cliente,parking,cobro_repositorio)
            print('-'*50)
        elif(opcion == 3):
            print('-'*50)
            print('Depositar abonados')
            dni = input(vista_cliente.pedirDni())
            matricula = input(vista_cliente.pedirMatricula())
            cliente_servicio.depositar_abonado(dni, matricula,parking,abono_repositorio)
            print('-'*50)
        elif(opcion == 4):
            print('-'*50)
            print('Retirar abonado')
            dni = input(vista_cliente.pedirDni())
            matricula = input (vista_cliente.pedirMatriculaRetirarVehiculo())
            cliente_servicio.retirar_abonado(dni,matricula,parking,abono_repositorio)
            print('-'*50)
        elif(opcion == 0):
            print('-'*50)
            print('Salir menu cliente')
            salir_submenu_cliente = True
    elif(opcion == 0):
        print('Salir')
        salir = True





