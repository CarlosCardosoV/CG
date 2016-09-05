#Cardoso Valencia Carlos Eric
#Computacion Grafica, Grupo 3
#Programa que calcula una transformacion geometricad dado un punto

import os
import math 

#Esta clase contiene las operaciones de transformacion geometrica
class Transformaciones():	
	
	def trasladar(self):
		punto_original = puntoOriginal() #Ingreso del punto original
		[d_x,d_y] = lecturaDatos('trasladar') #Ingreso de valores (desplazamientos, escalamiento o rotacion, segun el caso)
		[matriz_punto,matriz_mul]  = generarMatrices(punto_original,d_x,d_y,'trasladar') #Generacion de las matrices 
		punto_trasladado = multiplicarMatrices(matriz_punto,matriz_mul) #Producto de estas
		
		print "Punto trasladado =  " 
		print punto_trasladado

	def escalar(self):
		punto_original = puntoOriginal()
		[s_x,s_y] = lecturaDatos('escalar')
		[matriz_punto,matriz_mul] = generarMatrices(punto_original,s_x,s_y,'escalar')
		punto_escalado = multiplicarMatrices(matriz_punto,matriz_mul)
		
		print "Punto escalado = " 
		print punto_escalado		

	def rotar(self):
		punto_original = puntoOriginal()
		angulo = lecturaDatos('rotar')
		[matriz_punto,matriz_mul] = generarMatrices(punto_original,angulo,angulo,'rotar')
		punto_rotado = multiplicarMatrices(matriz_punto,matriz_mul)
		
		print "Punto aplicando una rotacion = " 
		print punto_rotado
	
	def ayuda(self):
		print ">>"
		print("trasladar: Calcula la traslacion de un punto dado ")
		print("escalar: Calula el escalamiento de un punto dado")
		print("rotar: Rotacion dado un punto")
		print("salir: Cerrar la consola")

	def salir(self):
		print " "	

	def limpiar(self):
		os.system('cls')

def lecturaDatos(tipo_transformacion):

	if tipo_transformacion == 'trasladar':
		d_x = raw_input('Desplazamiento en x:')
		d_y = raw_input('Desplazamiento en y:')

		return d_x,d_y
	
	if tipo_transformacion == 'escalar':
		s_x = raw_input('Escalamiento en x:')
		s_y = raw_input('Escalamiento en y:')

		return s_x,s_y

	if tipo_transformacion == 'rotar':
		angulo = raw_input('Valor del angulo;')

		return angulo

def puntoOriginal():
	punto_original = [0]*3
	print "Punto original"
	punto_original[0] = input('Coordenada en x:')
	punto_original[1] = input('Coordenada en y:')
	punto_original[2] = 1

	return punto_original
	

def generarMatrices(punto,valor1,valor2,tipo_transformacion):
	
	if tipo_transformacion == 'trasladar':
		matriz_punto = [ [punto[0],0,0],[punto[1],0,0],[1,0,0] ]
		matriz_mul = [[1,0,int(valor1)],[0,1,int(valor2)],[0,0,1]]
		
	if tipo_transformacion == 'escalar':
		matriz_punto = [ [punto[0],0,0],[punto[1],0,0],[1,0,0] ]
		matriz_mul = [[int(valor1),0,0],[0,int(valor2),0],[0,0,1]]
		
	if tipo_transformacion == 'rotar':
		sen_ang = math.sin( int(valor1) )
		cos_ang = math.cos( int(valor1) )
		matriz_punto = [ [punto[0],0,0],[punto[1],0,0],[1,0,0] ]
		matriz_mul = [[cos_ang,-sen_ang,0] ,[sen_ang,cos_ang,1] ,[0,0,1]]
	
	return matriz_punto,matriz_mul

def multiplicarMatrices(matriz_punto,matriz_mul):
	#Creacion de la matriz producto
	matriz_producto = []
	for i in range(len(matriz_mul)):
		matriz_producto.append( [0] * len(matriz_mul) )

	#Producto entre las matrices Punto y la que contiene los valores
	for i in range(len(matriz_mul)):
		for j in range(len(matriz_mul)):
			for k in range(len(matriz_producto)):
				matriz_producto[i][j] += matriz_mul[i][k] * matriz_punto[k][j]

	#Asignacion a las coordenasas del nuevo punto
	punto_modificado = [None]*len(matriz_punto)
	punto_modificado[0] = matriz_producto[0][0]
	punto_modificado[1] = matriz_producto[1][0]
	punto_modificado[2] = matriz_producto[2][0]

	return punto_modificado

#Simulacion de una consola de comandos. Los elementos  se guardan en un diccionario como un switch
def shell():
	print"\n"
	print ">>"
	print "Transformaciones geometricas: teclear ayuda para ver lista de comandos"
	cmd = Transformaciones()
	comando = "entrar" #PARA ENTRAR AL CICLO
	while(comando != "salir"):
		comandos = {'ayuda': cmd.ayuda,'trasladar':cmd.trasladar,'escalar':cmd.escalar,'rotar':cmd.rotar,'limpiar': cmd.limpiar, 'salir': cmd.salir }
		comando = raw_input('>>')		
		try:
			comandos[comando]()
		except:
			print (" '%s' no se reconoce como un comando. Teclea 'ayuda' para ver lista de comandos" %comando)

shell()