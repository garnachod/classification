# -*- coding: utf-8 -*-
import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from Clasificadores.RedNeuronalBlist import RedNeuronalBlist
from Particionado.DivisionPorcentual import DivisionPorcentual
from Particionado.Particion import Particion
from RW.LectorARFF import LectorARFF
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

	

	#random.seed(2)

	lector = LectorARFF()
	instances = lector.leerFichero("../data/entrenamiento.arff")
	instances.normaliza()
	
	porcentajeParticionado = float(0.50)
	particionado = DivisionPorcentual()
	particionado.setPorcentajeTrain(porcentajeParticionado)
	particion = particionado.generaParticionesProporcional(instances)
	
	
	print "Multilayer Perceptron"
	clasificador = RedNeuronalBlist()
	clasificador.setParameters('nNeuronas=' + str(50))
	clasificador.setParameters('alpha=' + str(0.01))
	clasificador.setParameters('nEpocas=500')
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

