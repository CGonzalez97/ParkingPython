# Carlos González Lozano - Proyecto parking con python  

El programa se ejecutará dentro del archivo index.py.  
Consta de persistencia y concurrencia con hilos. Esto último no es del todo necesario ya que despues de modificar algún repositorio se hace un guardado,  
pero me pareción interesante investigarlo a pesar de que se pudiera prescindir de ello tal y como tengo planteado el programa.  

Las excepciones personalizadas, las lanzan los métodos de los servicios y se capturan en el método principal del programa ( correr_programa() ).  

La persistencia se implementa mediante dos métodos en cada repositorio, cargar() y guardar(). Los datos se guardarán en el fichero .pckl que le corresponda al repositorio,  
dichos ficheros se encuentran en la carpeta persistencia.  

## Servicios  

### ClienteServicio  

Este servicio manejará las funciones que se ejecutarán desde el menú de cliente. Son:  

-depositarVehiculo(): modifica el atributo de ocupada de una plaza del parking que sea del mismo tipo que el vehículo introducido, no está abonada, y esté libre,   
además de generar el ticket.  

-retirarVehiculo():Modifica el atributo de ocupada de una plaza del mismo tipoque el vehículo introducido, no está abonada, y no esté libre, pidiendo previamente el pin del   ticket y la matrícula.    

-depositar_abonado():Modifica el atributo plaza_ocupada del abono, y ocupada de la plaza, tras pedir el dni del abonado y hacer las comprobaciones necesarias.  

-retirar_abonado():Modifica el atributo plaza_ocupada del abono, y ocupada de la plaza, tras pedir el dni del abonado y hacer las comprobaciones necesarias. 


### ParkingServicio

Este servicio manejará las acciones del menú parking.  

-informar_plazas(): muestra el estado de todas las plazas del parking haciendo doce grupos en base a tres factores, el tipo de plaza, si está abonada, y si está ocupada. 

-facturar(): calcula cuanto se ha recaudado entre dos fechas proporcionadas sin tener en cuenta los abonos.  

-crear_fecha_cancelacion(): es un método auxiliar para otros de la clase, se le proporciona una fecha y el plazo de abono, y en función de estos calcula la fecha de cancelación 
que le correspondería a un abono con dicha fecha y plazo.  

-facturacion_abono_concreto():se le pasa un plazo, y en función del mismo devuelve el precio que le correspondería.

-dar_alta_abono(): crea un abono y modifica una plaza del parking que no está abonada ni ocupada como abonada.  

-mostrar_abonos():muestra todos los abonos que hay con varios de sus datos.  

-mostrar_abonos_caducan_mes(): muestra los abonos que caducan entre la fecha actual y treinta días despues.  

-mostrar_abonos_caducan_diez(): muestra los abonos que caducan entre la fecha actual y diez días después.  

-calcular_anuales(): calcula la cuantía de dinero de los abonos anuales que están vigentes en ese momento.  

-consultar_abonados(): muestran los abonos anuales guardados.  

-eliminar_datos_abonado(): elimina los datos del abonado que se indique, manteniendo el resto de datos del abono.  

-modificar_abono(): modifica los datos de un abono.  

-renovar_abono(): modifica la fecha de cancelación de un abono sumandole a su fecha de cancelación un periodo en función del plazo del mismo.  

