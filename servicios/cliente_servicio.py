from modelos.ticket import Ticket
from modelos.cobro import Cobro
from datetime import datetime

from modelos.vehiculo import Coche, Moto, Vehiculo_pmr


class Cliente_Servicio:
    def __init__(self):
        pass

    def depositarVehiculo(self,
                          vehiculo,
                          parking,
                          vista_cliente,
                          ticket_repositorio):
        ticket_resultado = None
        encontrado = False
        for i in parking.plazas:
            if (not encontrado and not i.abonada and not i.ocupada):
                if ((i.tipo == 'coche' and isinstance(vehiculo, Coche)) or
                        (i.tipo == 'moto' and isinstance(vehiculo, Moto)) or
                        (i.tipo == 'pmr' and isinstance(vehiculo, Vehiculo_pmr))):
                    print('Entra en la condicion')
                    encontrado = True
                    i.ocupada = True
                    ticket_creado = Ticket(vehiculo, i, datetime.now())
                    ticket_repositorio.lista_tickets.append(ticket_creado)
                    print(vista_cliente.plazaEncontrada())
                    print(ticket_creado)
        if (not encontrado):
            print(vista_cliente.plazaNoEncontrada())

    def retirarVehiculo(self,
                        matricula,
                        pin,
                        ticket_repositorio,
                        vista_cliente,
                        parking,
                        cobro_repositorio):
        encontrado = False
        if (len(ticket_repositorio.lista_tickets) > 0):
            for i in ticket_repositorio.lista_tickets:
                if (i.vehiculo.matricula == matricula):
                    if (i.pin == pin):
                        for j in parking.plazas:
                            # if(i.vehiculo.tipo == j.tipo and
                            # j.ocupada and not j.abonada and
                            # not encontrado):
                            if ((isinstance(i.vehiculo, Coche) and j.tipo == 'coche') or
                                    (isinstance(i.vehiculo, Moto) and j.tipo == 'moto') or
                                    (isinstance(i.vehiculo, Vehiculo_pmr) and j.tipo == 'pmr') and
                                    not encontrado and j.ocupada and not j.abonada):
                                j.ocupada = False
                                encontrado = True
                        #print('Diferencia de fecha deposito y retirada: ',((datetime.now() - i.fechaDeposito).total_seconds()/60))
                        tiempo_a_cobrar = abs((datetime.now() - i.fechaDeposito).total_seconds()/60)
                        cuantia_cobro = i.vehiculo.tarifa * tiempo_a_cobrar
                        cobro_a_introducir = Cobro(datetime.now(),cuantia_cobro,i)
                        #print('Cuantia del cobro:',cuantia_cobro,'tiempo a cobrar:',tiempo_a_cobrar,'tarifa_v:',i.vehiculo.tarifa,'operacion:',(cuantia_cobro*i.vehiculo.tarifa))
                        # cobro_repositorio.lista_cobros.append(Cobro(datetime.now(),
                        #                                             cuantia_cobro,  # i.vehiculo.tarifa,
                        #                                             i))
                        #print('cobro a introducir:',cobro_a_introducir.cobro_final,cobro_a_introducir.fecha_salida)
                        cobro_repositorio.lista_cobros.append(cobro_a_introducir)
                        print(vista_cliente.confirmarRetiradaDeVehiculo())
                    else:
                        print(vista_cliente.indicarPinErroneo())
                else:
                    print(vista_cliente.indicarMatriculaNoEncontrada())
        else:
            print(vista_cliente.indicarNoHayTickets())

    def depositar_abonado(self,
                          dni,
                          matricula,
                          parking,
                          abono_repositorio):
        print('Entra a depositar abonado')
        abono_entontrado = False
        plaza_encontrada = False
        if (len(abono_repositorio.lista_abonos) <= 0):
            print('No hay abonos')
        for i in abono_repositorio.lista_abonos:
            # print(i.mostrar())
            # print(f'dni pasado {dni}, dni abono {i.cliente.dni}, matricula pasada {matricula}, matricula abono {i.cliente.vehiculo.matricula}')
            # print(not abono_entontrado and i.cliente.dni == dni and i.cliente.vehiculo.matricula == matricula and not i.plaza_ocupada)
            # print(not abono_entontrado)
            # print(i.cliente.dni == dni)
            # print(i.cliente.vehiculo.matricula == matricula)
            # print(not i.plaza_ocupada)
            if (not abono_entontrado and
                    i.cliente.dni == dni and
                    i.cliente.vehiculo.matricula == matricula and
                    not i.plaza_ocupada):
                print('Ha encontrado abono con esos DNI y  matricula')
                abono_entontrado = True
                #plaza_encontrada = False
                for j in parking.plazas:
                    # if(not plaza_encontrada and
                    # j.tipo == i.cliente.vehiculo.tipo and
                    # not j.ocupada and j.abonada):
                    if (not plaza_encontrada and
                            ((j.tipo == 'coche' and isinstance(i.cliente.vehiculo, Coche)) or
                             (j.tipo == 'moto' and isinstance(i.cliente.vehiculo, Moto)) or
                             (j.tipo == 'pmr' and isinstance(i.cliente.vehiculo, Vehiculo_pmr))) and
                            not j.ocupada and j.abonada):
                        print('Ha encontrado plaza de ese tipo de vehiculo que no está ocupada y está abonada')
                        plaza_encontrada = True
                        j.ocupada = True
                        i.plaza_ocupada = True
                        print('Vehiculo depositado en plaza abonada.')
        if(not abono_entontrado):
            print('No hay abono con esos datos')
        elif(not plaza_encontrada):
            print('No hay plaza que coincida con su abono')
    def retirar_abonado(self,
                        dni,
                        matricula,
                        parking,
                        abono_repositorio):
        abono_encontrado = False
        for i in abono_repositorio.lista_abonos:
            if (not abono_encontrado and
                    i.cliente.dni == dni and
                    i.plaza_ocupada):
                plaza_encontrada = False
                for j in parking.plazas:
                    if (not plaza_encontrada and
                            #(j.tipo == i.cliente.vehiculo.tipo) and
                            ((j.tipo == 'coche' and isinstance(i.cliente.vehiculo,Coche)) or
                            (j.tipo == 'moto' and isinstance(i.cliente.vehiculo,Moto)) or
                            (j.tipo == 'pmr' and isinstance(i.cliente.vehiculo,Vehiculo_pmr)))and
                            j.ocupada and j.abonada):
                        plaza_encontrada = True
                        j.ocupada = False
                        i.plaza_ocupada = False
