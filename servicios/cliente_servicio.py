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

                        cobro_repositorio.lista_cobros.appends(Cobro(datetime.now(),
                                                                     i.vehiculo.tarifa,
                                                                     i))
                        vista_cliente.confirmarRetiradaDeVehiculo()
                    else:
                        vista_cliente.indicarPinErroneo()
                else:
                    vista_cliente.indicarMatriculaNoEncontrada()
        else:
            vista_cliente.indicarNoHayTickets()
