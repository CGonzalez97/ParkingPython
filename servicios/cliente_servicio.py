from modelos.ticket import Ticket
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
