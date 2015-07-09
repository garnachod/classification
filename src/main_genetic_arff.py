import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from RW.LectorARFF import LectorARFF
from Clasificadores.Genetic import Genetic
from Clasificadores.GeneticECM import GeneticECM
from Particionado.DivisionPorcentual import DivisionPorcentual
from Particionado.Particion import Particion

def calculaError(clasificador, instances):
	error = 0.0
	erroresPorClase = {}
	aciertosPorClase = {}
	for clase in instances.getClases():
		erroresPorClase[clase] = 0
		aciertosPorClase[clase] = 0

	for instance in instances.getListInstances():
		clase = instance.getClase()
		prediccion, ecm = clasificador.classifyInstance(instance)
		#print prediccion
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


if __name__ == '__main__':
	lector = LectorARFF()
	instances = lector.leerFichero("../data/spam.arff")
	instances.normaliza()

	porcentajeParticionado = float(0.66)
	particionado = DivisionPorcentual()
	particionado.setPorcentajeTrain(porcentajeParticionado)
	particion = particionado.generaParticionesProporcional(instances)

	print "Multilayer genetic"
	clasificador = GeneticECM()
	clasificador.buildClassifier(particion.getTrain())

	print "Error TRAIN:"
	calculaError(clasificador, particion.getTrain())
	if porcentajeParticionado != 1.0:
		print "Error TEST:"
		calculaError(clasificador, particion.getTest())