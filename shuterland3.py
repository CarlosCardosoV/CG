#RECORTE DE PUNTOS POR COHEN-SHUTERLAND

import os
import random

class Ventana():
	#Constructor inicial
	def __init__(self,ancho,altura,vertice_inf_izq):	
		self.ancho = ancho
		self.altura = altura
		self.vertice_inf_izq = vertice_inf_izq

class Menu():
	def ayuda(self):
		print ">>"
		print("ingresar: Ingresa una serie de puntos")
		print("generar: Generar una serie de puntos aleatorios dado un rango")
		print("limpiar: Limpiar la pantalla")
		print("salir: Cerrar la consola")

	#Shuterland para una serie de puntos dados por el usuario
	def ingresar(self):
		[lista_x,lista_y] = lecturaPuntos()
		lista_regiones = asignarRegiones(lista_x,lista_y)
		imprimirDatos(lista_x,lista_y,lista_regiones)
		[lista_or,zipped] = operacionOr(lista_regiones)

		posicion = [None]*len(zipped)
		print "**Operacion OR resultados"
		for i in range(len(lista_or)):
			if lista_or[i] == 0:
				print "  Linea %d se dibuja en la ventana: " %(i+1)
			else:
				print "  Linea %d prosigue con el algoritmo" %(i+1)
				posicion[i] = i

		
		lista_and = operacionAnd(zipped)
		print "**Operacion AND resultados"
		for i in range(len(lista_and)):
			if posicion[i] == i :
				if lista_and[i] == 0:
					print "  Linea %d se recorta (pasa a algoritmo de Lian-Barsky)" %(posicion[i]+1)
				else:
					print "  Linea %d se descarta (no pasa al algoritmo de Lian-Barsky)" %(posicion[i]+1)


	#Shuterland para puntos generados aleatoriamente
	def generar(self):
		[lista_x,lista_y] = generarPuntos()
		lista_regiones = asignarRegiones(lista_x,lista_y)
		imprimirDatos(lista_x,lista_y,lista_regiones)
		[lista_or,zipped] = operacionOr(lista_regiones)
		
		posicion = [None]*len(zipped) 	#Crear un arreglo de posiciones para identificar a que puntos les aplicamos la and

		print "**Operacion OR resultados"
		for i in range(len(lista_or)):
			if lista_or[i] == 0:
				print "  Linea %d se dibuja en la ventana " %(i+1)
			else:
				print "  Linea %d prosigue con el algoritmo" %(i+1)
				posicion[i] = i

		lista_and = operacionAnd(zipped)
		print "**Operacion AND resultados"
		for i in range(len(lista_and)):
			if posicion[i] == i :
				if lista_and[i] == 0:
					print "  Linea %d se recorta (pasa a algoritmo de Lian-Barsky)" %(posicion[i]+1)
				else:
					print "  Linea %d se descarta (no pasa al algoritmo de Lian-Barsky)" %(posicion[i]+1)

	def salir(self):
		print " "	

	def limpiar(self):
		os.system('cls')


#Ingreso de puntos por parte del usuario
def lecturaPuntos():
	numero_lineas = 5
	aux = 0

	#Listas que almacenan los valores de las coordenadas de los puntos 
	lista_x = [0]*2*numero_lineas  
	lista_y= [0]*2*numero_lineas

	for i in range(numero_lineas):
		print "**Linea %d" %(i+1)
		for j in range(2):
			print " Punto %d" %(j+1)
		
			try:
				lista_x[aux] = input("  Coordenada en x:")
				lista_y[aux] = input("  Coordenada en y:")
				aux+=1
			except:
				print "Solo numeros reales!"

	return lista_x,lista_y

#Generacion de una lista de puntos aleatorios dado un rango minimo y uno maximo
def generarPuntos():
	numero_lineas = 5
	aux = 0
	lista_x = [0]*2*numero_lineas  
	lista_y= [0]*2*numero_lineas
	min_valor = input("Rango inferior:")
	max_valor = input("Rango superior:")

	for i in range(numero_lineas):
		for j in range(2):
			lista_x[aux] = random.randint(min_valor, max_valor)
			lista_y[aux] = random.randint(min_valor, max_valor)
			aux+=1

	return lista_x,lista_y


#Asigna cada punto a una respectiva region de las 9 disponibles. Es decir, cada punto se  asocia con un codigo binario de 4 bits
def asignarRegiones(lista_x,lista_y):
	#Definiendo las regiones
	region1 = "1010"	#Region superior izquierda
	region2 = "0010"	#Region superior central
	region3 = "0110"	#Region superior derecha
	region4 = "1000"	#Region cental izquierda
	region5 = "0000"    #Region central(ventana)
	region6 = "0100"    #Region central derecha
	region7 = "1001"	#Region inferior izquierda
	region8 = "0001"	#Region inferior central
	region9 = "0101"	#Region inferior derecha

	lista_regiones = [None]*len(lista_x)
	#Valores para la ventana
	ancho = 640
	altura = 480
	vertice_inf_izq = (50,50)
	v = Ventana(ancho,altura,vertice_inf_izq)

	#Asinacion de los puntos que caen en cada region
	for i in range( len(lista_x) ):
		#Region 1
		if (lista_x[i] < v.vertice_inf_izq[0]) and (lista_y[i] > (v.vertice_inf_izq[1]+v.altura)):
			lista_regiones[i] = region1

		#Region 2
		if ( v.vertice_inf_izq[0] < lista_x[i] < (v.vertice_inf_izq[0]+v.ancho) ) and (lista_y[i] > (v.vertice_inf_izq[1]+v.altura)):
			lista_regiones[i] = region2

		#Region 3
		if (lista_x[i] > (v.vertice_inf_izq[0]+v.ancho) ) and (lista_y[i] > (v.vertice_inf_izq[1]+v.altura)):
			lista_regiones[i] = region3

		#Region 4
		if ( lista_x[i] < v.vertice_inf_izq[0] ) and  (v.vertice_inf_izq[1] < lista_y[i] < (v.vertice_inf_izq[1] + v.altura)):
			lista_regiones[i] = region4

		#Region 5
		if (v.vertice_inf_izq[0] < lista_x[i] < (v.vertice_inf_izq[0]+v.ancho) ) and (v.vertice_inf_izq[1] < lista_y[i] < (v.vertice_inf_izq[1] + v.altura)) : 
			lista_regiones[i] = region5

		#Region 6
		if (lista_x[i] > (v.vertice_inf_izq[0]+v.ancho) ) and (v.vertice_inf_izq[1] < lista_y[i] < (v.vertice_inf_izq[1] + v.altura)):
			lista_regiones[i] = region6

		#Region 7
		if ( lista_x[i] < v.vertice_inf_izq[0] ) and (lista_y[i] < v.vertice_inf_izq[1]):
			lista_regiones[i] = region7

		#Region 8
		if (v.vertice_inf_izq[0] < lista_x[i] < (v.vertice_inf_izq[0]+v.ancho) ) and (lista_y[i] < v.vertice_inf_izq[1]):
			lista_regiones[i] = region8

		#Region 9
		if (lista_x[i] > (v.vertice_inf_izq[0]+v.ancho) ) and (lista_y[i] < v.vertice_inf_izq[1]):
			lista_regiones[i] = region9
	
	return lista_regiones

#Para cada linea, realizar operacion OR con los valores de sus puntos extremos, para
#decidir si se dibuja (OR = 0000) o se prosigue con el algoritmo (OR != 0000) 
def operacionOr(lista_regiones):
	lista_or = [None]*(len(lista_regiones)/2)
	#Ordenamos por pares a la lista_regiones para poder operarlos mas facilmente
	for i in range(len(lista_regiones)):
		lista_regiones[i] = int(lista_regiones[i])
	
	zipped = zip(lista_regiones[0::2], lista_regiones[1::2]) #http://stackoverflow.com/questions/4647050/collect-every-pair-of-elements-from-a-list-into-tuples-in-python
	lista_or = [x|y for (x,y) in zipped] #http://stackoverflow.com/questions/29471260/sum-of-elements-stored-inside-a-tuple
	
	return lista_or,zipped

#Para cada linea cuya operacion OR de sus puntos fue diferente a cero, realizar operacion AND con sus puntos extremos
#para decidir si se recorta (AND=0000) o se descarta (AND != 0000)
def operacionAnd(zipped):
	lista_and = [x&y for (x,y) in zipped]
	return lista_and


#Metodo de impresion de todos los puntos por columnas 
def imprimirDatos(lista_x,lista_y,lista_regiones):
	aux2 = 0
	print('{0:10s} {1:30s} {2:40s}'.format('			Valor en X', '	  Valor en Y',	'Codigo'))
	for i in range(len(lista_y)/2):
		print "**Linea %d" %(i+1)
		for j in range(2):
			print('{0:5s} {1:20d} {2:20d} {3:14s} {4:s}'.format("Punto %d",lista_x[aux2], lista_y[aux2],"\t",lista_regiones[aux2]) %(j+1) )
			aux2+=1

################################################################################################################
#Simulacion de una consola de comandos. Los elementos  se guardan en un diccionario como un switch
def shell():
	print"\n"
	print ">>"
	print "Algoritmo Cohen-Shutherland: teclear ayuda para ver lista de comandos"
	cmd = Menu()
	comando = "entrar" #PARA ENTRAR AL CICLO
	while(comando != "salir"):
		comandos = {'ayuda': cmd.ayuda,'ingresar':cmd.ingresar,'generar':cmd.generar,'limpiar': cmd.limpiar, 'salir': cmd.salir }
		comando = raw_input(">>")		
		try:
			comandos[comando]()
		except:
			print (" '%s' no se reconoce como un comando. Teclea 'ayuda' para ver lista de comandos" %comando)

shell()