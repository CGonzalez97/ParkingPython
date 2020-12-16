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
salir_submenu_cliente = False
salir_submenu_parking = False
salir_submenu_abonos = False
#opcion = None

while not salir:
    opcion = int(input(vista_general.preguntar_tipo_usuario()))
    if(opcion == 1):
        #Menu gestor
        print(vista_parking.introducir_a_menu_gestor())
        while not salir_submenu_parking:
            opcion = int(input(vista_parking.mostrarOpcionesParkin()))
            if(opcion == 1):
                print('Estado parking')
            elif(opcion == 2):
                print('Facturación')
            elif(opcion == 3):
                print('Consulta de abonados')
            elif(opcion == 4):
                print('Menu abonos')
                while not salir_submenu_abonos:
                    opcion = int(input(vista_parking.mostrarMenuAbonos()))
                    if(opcion == 1):
                        print('Mostrar abonos')
                    elif(opcion == 2):
                        print('Dar alta a un abono')
                    elif(opcion == 3):
                        print('Modificar abono')
                    elif(opcion == 4):
                        print('Eliminar abono')
                    elif(opcion == 5):
                        print('Mostrar caducan este mes')
                    elif(opcion == 6):
                        print('Mostrar caducan diez días')
                    elif(opcion == 7):
                        print('Total abonos anuales')
                    elif(opcion == 0):
                        print('Salir submenu abonos')
            elif(opcion == 0):
                print('Salir menu parking')
    elif(opcion == 2):
        #Menu cliente
        opcion = int(input(vista_cliente.preguntarOpcionCliente()))
        if(opcion == 1):
            print('Depositar vehiculo')
        elif(opcion == 2):
            print('Retirar vehiculo')
        elif(opcion == 3):
            print('Retirar abonados')
        elif(opcion == 4):
            print('Retirar abonado')
        elif(opcion == 0):
            print('Salir menu cliente')
    elif(opcion == 0):
        print('Salir')





