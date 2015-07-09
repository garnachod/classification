# -*- coding: utf-8 -*-
from heapq import heappush, heappop
from Instance import Instance
from Instances import Instances
from operator import add,mul
from textblob import TextBlob
from NodosPalabras.Nodo import Nodo
import math

class RedPalabras(object):
	"""docstring for Clasificador"""
	def __init__(self):
		super(RedPalabras, self).__init__()
		self.nodosPorClase = {}
		self.clases = {}

	"""parametros es un string de configuracion para el clasificador"""
	"""para KNN por ejemplo k=11, para una red reuronal,numero de capas
	 	nl=2... cada clasificador se puede preguntar con getCapabilities()"""
	def setParameters(self, parametros):
		raise NotImplementedError( "Should have implemented this" )
		
	"""data es un array de instancias"""
	def buildClassifier(self, data):
		#todas las instancias de este clasificador se asumen [texto, clase]
		self.clases = list(data.getClases())
		for clase in self.clases:
			self.nodosPorClase[clase] = {}

		

		for instance in data.getListInstances():
			texto = instance.getElementAtPos(0)
			clase = instance.getElementAtPos(1)
			textB = TextBlob(texto)

			nodoAnterior = None
			for palabra in textB.words:
				palabra = palabra.lower()
				if palabra in self.nodosPorClase[clase]:
					if nodoAnterior is None:
						nodoAnterior = self.nodosPorClase[clase][palabra]
					else:
						nodo = self.nodosPorClase[clase][palabra]
						if nodoAnterior.isConexo(palabra):
							nodoAnterior.sumaAlPeso(palabra, 0.1)
						else:
							#nodo.setConexo(nodoAnterior)
							nodoAnterior.setConexo(nodo)
						nodoAnterior = nodo
				else:
					#se crea el nodo porque no existe en esta clase
					nodo = Nodo(palabra)
					self.nodosPorClase[clase][palabra] = nodo
					if nodoAnterior is None:
						pass
					else:
						#nodo.setConexo(nodoAnterior)
						nodoAnterior.setConexo(nodo)
					nodoAnterior = nodo


	"""se clasifica una sola instancia, retornando la clase, int"""
	def classifyInstance(self, instance):
		#todas las instancias de este clasificador se asumen [texto, clase]
		texto = instance.getElementAtPos(0)
		clase = instance.getElementAtPos(1)
		textB = TextBlob(texto)

		pesoClase = {}
		
		for clase in self.clases:
			pesoClase[clase] = 0
			nodoAnterior = None
			for palabra in textB.words:
				if palabra in self.nodosPorClase[clase]:
					if nodoAnterior is None:
						nodoAnterior = self.nodosPorClase[clase][palabra]
					else:
						if nodoAnterior.isConexo(palabra):
							peso = nodoAnterior.getPeso(palabra)
							pesoClase[clase] += peso
						else:
							#por ahora nada, pero se debería aplicar dikstra
							pesoClase[clase] += 0
				else:
					pesoClase[clase] += 0

		mejorClase = None
		mejorClaseN = 0
		for clase in self.clases:
			if mejorClase is None:
				mejorClase = clase
				mejorClaseN = pesoClase[clase]
			else:
				if mejorClaseN < pesoClase[clase]:
					mejorClase = clase
					mejorClaseN = pesoClase[clase]

		return mejorClase

	"""retorna un String JSON para que el Clasificador se pueda guardar en un fichero o donde sea necesario"""
	def saveClassifierToJSON(self):
		raise NotImplementedError( "Should have implemented this" )

	def restoreClassifierFromJSON(self, jsonObj):
		raise NotImplementedError( "Should have implemented this" )

	"""retorna un string con el funcionamiento del Clasificador"""
	def getCapabilities(self):
		raise NotImplementedError( "Should have implemented this" )

	"""Hace que el clasificador entre en modo debug o no"""
	def setDebug(self, value):
		raise NotImplementedError( "Should have implemented this" )

