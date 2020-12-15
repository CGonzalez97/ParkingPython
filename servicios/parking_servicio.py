from datetime import datetime
#pip install dateutil
#from dateutil.relativedelta import relativedelta

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

        def  facturar(vistaParkin, cobro_repositorio, vista_parking):
            cuantia = 0
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
                if(i.fecha_salida > fecha_inicial
                and i.fecha_salida < fecha_final):
                    cuantia += i.cobro_final

            return cuantia

        #---------------------------------------------------------

        #ABONOS

        #Crear fecha cancelacion
        #use_date = use_date+relativedelta(months=+1) <- ¿usar?
        def crear_fecha_cancelacion(fecha_ini, plazo):
            if(plazo == 'mensual'):
                dummy1 = None
            elif(plazo == 'trimestral'):
                dummy2 = None
            elif(plazo == 'semestral'):
                dummy3 = None
            elif(plazo == 'anual'):
                dummmy4 = None


