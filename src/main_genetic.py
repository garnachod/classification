import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from RW.LectorNeuro import LectorNeuro
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
		prediccion = clasificador.classifyInstance(instance)
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
	lector = LectorNeuro()
	instances = lector.leerFichero("../data/problema_real1.txt")
	instances.normaliza()

	porcentajeParticionado = float(0.8)
	particionado = DivisionPorcentual()
	particionado.setPorcentajeTrain(porcentajeParticionado)
	particion = particionado.generaParticionesProporcional(instances)
	
	print "Multilayer genetic"
	clasificador = GeneticECM()
	clasificador.buildClassifier(instances)

	print "Error TRAIN:"
	calculaError(clasificador, instances)
	if porcentajeParticionado != 1.0:
		print "Error TEST:"
		calculaError(clasificador, particion.getTest())