import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from Clasificadores.KNN import KNN
from Clasificadores.KNNGenetic import KNNGenetic
from Clasificadores.RedPalabras import RedPalabras
from Clasificadores.RedPalabrasGenetic import RedPalabrasGenetic
from Particionado.DivisionPorcentual import DivisionPorcentual
from Particionado.Particion import Particion
from RW.LectorNeuro import LectorNeuro
from RW.LectorARFF import LectorARFF
from RW.LectorIMDB import LectorIMDB
from Instance import Instance
from Instances import Instances

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

if __name__ == '__main__':
	lector = LectorIMDB()
	instances = lector.leerFichero('../data/imdb_labelled.txt')
	#instances.normaliza()
	porcentajeParticionado = 0.8
	particionado = DivisionPorcentual()
	particionado.setPorcentajeTrain(porcentajeParticionado)
	particion = particionado.generaParticionesProporcional(instances, True)

	#clasificador = KNN()
	#clasificador = RedPalabras()
	#clasificador.buildClassifier(particion.getTrain())
	clasificador = RedPalabrasGenetic()
	clasificador.buildClassifier(particion.getTrain())

	print "err Entrenamiento"
	calculaError(clasificador, particion.getTrain())
	print "err Test"
	calculaError(clasificador, particion.getTest())