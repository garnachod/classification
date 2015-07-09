# -*- coding: utf-8 -*-
import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from Clasificadores.RandomNeuralNetwork import RandomNeuralNetwork
from Clasificadores.RedNeuronal import RedNeuronal
from Clasificadores.GeneticECM import GeneticECM
from Clasificadores.RedNeuronalBlist import RedNeuronalBlist
from Particionado.DivisionPorcentual import DivisionPorcentual
from Particionado.Particion import Particion
from RW.LectorNeuro import LectorNeuro
from Instance import Instance
from Instances import Instances
from time import time
import random


def calculaError(clasificador, instances): 
	error = 0.0
	erroresPorClase = {}
	aciertosPorClase = {}
	for clase in instances.getClases():
		erroresPorClase[clase] = 0
		aciertosPorClase[clase] = 0

	for instance in instances.getListInstances():
		clase = instance.getClase()
		prediccion = clasificador.classifyInstance(instance)
		#print "clase: " + str(clase) + " prediccion: " + str(prediccion)

		if prediccion != clase:
			erroresPorClase[clase] += 1
			error += 1.0
		else:
			aciertosPorClase[clase] += 1 

	procentajeError = error / float(instances.getNumeroInstances())
	print 'Error medio: ' + str(procentajeError)
	for clase in instances.getClases():
		sumaAux = float(erroresPorClase[clase] + aciertosPorClase[clase])
		print '\t'+ clase + ' fallos: ' + str(erroresPorClase[clase]) + ' aciertos: ' + str(aciertosPorClase[clase]) + ' porcentaje: ' + str(erroresPorClase[clase] / sumaAux)

def returnError(clasificador, instances):
	error = 0.0

	for instance in instances.getListInstances():
		clase = instance.getClase()
		prediccion = clasificador.classifyInstance(instance)
		#print "clase: " + str(clase) + " prediccion: " + str(prediccion)

		if prediccion != clase:
			error += 1.0

	procentajeError = error / float(instances.getNumeroInstances())
	return procentajeError

if __name__ == '__main__':

	if len(sys.argv) != 6:
		print "Error en la llamada. Se esperan los siguientes argumentos:"
		print "\t1.- Nombre del fichero con los datos del problema."
		print "\t2.- El porcentaje del conjunto de train. Expresar como un numero entre 0 y 1 utilizando el punto como divisor decimal."
		print "\t3.- La tasa de aprendizaje."
		print "\t4.- El numero de neuronas de la capa oculta."
		print "\t5.- El nombre del fichero donde debe escribirse el error cuadratico medio en cada epoca. Se borrara el fichero si ya existe."
		print "Ejemplo de llamada: python main.py xor.txt 1 0.1 2 xor_error.txt"
		sys.exit(-1)

	#random.seed(2)

	lector = LectorNeuro()
	instances = lector.leerFichero(sys.argv[1])
	instances.normaliza()
	
	porcentajeParticionado = float(sys.argv[2])
	particionado = DivisionPorcentual()
	particionado.setPorcentajeTrain(porcentajeParticionado)
	particion = particionado.generaParticionesProporcional(instances)
	
	"""
	print "Multilayer Perceptron Random"
	clasificador = RandomNeuralNetwork()
	clasificador.setParameters('nNeuronas=' + sys.argv[4])
	clasificador.setParameters('alpha=' + sys.argv[3])
	clasificador.setParameters('nEpocas=1000')
	clasificador.setParameters('debugFile=' + sys.argv[5])
	clasificador.setDebug(False)
	start_time = time()
	if porcentajeParticionado != 1.0:
		clasificador.buildClassifier(particion.getTrain())
	else:
		clasificador.buildClassifier(particion.getTrain())
	elapsed_time = time() - start_time
	print("Elapsed time: %0.10f seconds." % elapsed_time)

	print "Error TRAIN:"
	calculaError(clasificador, particion.getTrain())
	if porcentajeParticionado != 1.0:
		print "Error TEST:"
		calculaError(clasificador, particion.getTest())
	"""
	print "Multilayer Perceptron"
	clasificador = RedNeuronal()
	clasificador.setParameters('nNeuronas=' + sys.argv[4])
	clasificador.setParameters('alpha=' + sys.argv[3])
	clasificador.setParameters('nEpocas=100')
	clasificador.setParameters('debugFile=' + sys.argv[5])
	clasificador.setDebug(False)
	start_time = time()
	if porcentajeParticionado != 1.0:
		clasificador.buildClassifier(particion.getTrain())
	else:
		clasificador.buildClassifier(particion.getTrain())
	elapsed_time = time() - start_time
	print("Elapsed time: %0.10f seconds." % elapsed_time)

	print "Error TRAIN:"
	calculaError(clasificador, particion.getTrain())
	if porcentajeParticionado != 1.0:
		print "Error TEST:"
		calculaError(clasificador, particion.getTest())

	print "Multilayer Perceptron Blist"
	clasificador = RedNeuronalBlist()
	clasificador.setParameters('nNeuronas=' + sys.argv[4])
	clasificador.setParameters('alpha=' + sys.argv[3])
	clasificador.setParameters('nEpocas=100')
	clasificador.setParameters('debugFile=' + sys.argv[5])
	clasificador.setDebug(False)
	start_time = time()
	if porcentajeParticionado != 1.0:
		clasificador.buildClassifier(particion.getTrain())
	else:
		clasificador.buildClassifier(particion.getTrain())
	elapsed_time = time() - start_time
	print("Elapsed time: %0.10f seconds." % elapsed_time)

	print "Error TRAIN:"
	calculaError(clasificador, particion.getTrain())
	if porcentajeParticionado != 1.0:
		print "Error TEST:"
		calculaError(clasificador, particion.getTest())


	"""print "Multilayer Perceptron GENETIC"
	clasificador = GeneticECM()
	start_time = time()
	clasificador.buildClassifier(particion.getTrain())

	print "Error TRAIN:"
	calculaError(clasificador, particion.getTrain())
	if porcentajeParticionado != 1.0:
		print "Error TEST:"
		calculaError(clasificador, particion.getTest())

	elapsed_time = time() - start_time
	print("Elapsed time: %0.10f seconds." % elapsed_time)
	"""

	#fout = open("predicciones_nnet.txt", "w")

	# clasificador del nuevo
	"""instances = lector.leerFichero(sys.argv[6])
	for instance in instances.getListInstances():
		clase = clasificador.classifyInstance(instance)
		if int(clase) == 0:
			fout.write('0 1\n')
		else:
			fout.write('1 0\n')
"""
	#print clasificador.classifyInstance(instances.getListInstances()[4])
	#print (instances.getListInstances()[4]).getClase()

