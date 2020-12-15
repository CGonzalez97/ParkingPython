from modelos.ticket import Ticket
from modelos.cobro import Cobro
from datetime import datetime

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
            if(not encontrado and not i.abonada and not i.ocupada and i.tipo == vehiculo.tipo):
                encontrado = True
                i.ocupada = True
                ticket_repositorio.lista_tickets.appends(Ticket(vehiculo,
                                                                i,
                                                                datetime.now()))
                print(vista_cliente.plazaEncontrada())
            else:
                print(vista_cliente.plazaNoEncontrada())

    def retirarVehiculo(self,
                        matricula,
                        pin,
                        ticket_repositorio,
                        vista_cliente,
                        parking,
                        cobro_repositorio):
        encontrado = False
        if(len(ticket_repositorio.lista_tickets) > 0):
            for i in ticket_repositorio.lista_tickets:
                if(i.vehiculo.matricula == matricula):
                    if(i.pin == pin):
                        for j in parking.plazas:
                            if(i.vehiculo.tipo == j.tipo and
                            j.ocupada and not j.abonada and
                            not encontrado):
                                j.ocupadad = False
                                encontrado = True
                        tiempo_a_cobrar = abs((i.fechaDeposito - datetime.now()).minutes)
                        cuantia_cobro = i.vehiculo.tarifa * tiempo_a_cobrar
                        cobro_repositorio.lista_cobros.appends(Cobro(datetime.now(),
                                                                     cuantia_cobro,#i.vehiculo.tarifa,
                                                                     i))
                        vista_cliente.confirmarRetiradaDeVehiculo()
                    else:
                        vista_cliente.indicarPinErroneo()
                else:
                    vista_cliente.indicarMatriculaNoEncontrada()
        else:
            vista_cliente.indicarNoHayTickets()

    def depositar_abonado(self,
                         dni,
                         matricula,
                         parking,
                         abono_repositorio):
        abono_entontrado = False
        for i in abono_repositorio.lista_abonos:
            if(not abono_entontrado and
            i.dni == dni and
            i.matricula == matricula and
            not i.plaza_ocupada):
                abono_entontrado = True
                plaza_encontrada = False
                for j in parking.plazas:
                    if(not plaza_encontrada and
                    j.tipo == i.cliente.vehiculo.tipo and
                    not j.ocupada and j.abonada):
                        plaza_encontrada = True
                        j.ocupada = True
                        i.plaza_ocupada = True

    def retirar_abonado(self,
                        dni,
                        matricula,
                        parking,
                        abono_repositorio):
        abono_encontrado = False
        for i in abono_repositorio.lista_abonos:
            if(not abono_encontrado and
            i.cliente.dni == dni and
            i.plaza_ocupada):
                plaza_encontrada = False
                for j in parking.plazas:
                    if(not plaza_encontrada and
                    j.tipo == i.cliente.vehiculo.tipo and
                    j.ocupada and j.abonada):
                        plaza_encontrada = True
                        j.ocupada = False
                        i.plaza_ocupada = False



