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
import math

ticket_repositorio = Ticket_Repositorio()
cobro_repositorio = Cobro_Repositorio()
abono_repositorio = Abono_Repositorio()

cliente_servicio = Cliente_Servicio()
parking_servicio = Parking_Servicio()

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



