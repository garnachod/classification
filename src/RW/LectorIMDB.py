# -*- coding: utf-8 -*-
#solo usar para debug
import os, sys
lib_path = os.path.abspath('../../')
sys.path.append(lib_path)
#fin de solo usar para debug
import re
from src.Instances import Instances
from src.Instance import Instance
import string
import codecs

class LectorIMDB(object):
	"""docstring for LectorNeuro"""
	def __init__(self):
		super(LectorIMDB, self).__init__()
		self.delimiters = r'\t|\n|\r'


	def leerFichero(self, nombre_fichero):
		f = codecs.open(nombre_fichero, "r", "utf-8")
		#instancias al estilo WEKA
		instances = Instances()

		primeraLinea = f.readline()
		cadenasLinea = re.split(r'\t|\n|\r| ', primeraLinea)
		numeroEntradas = int(cadenasLinea[0])
		numeroClases = int(cadenasLinea[1])

		for i in range(0, numeroEntradas):
			instances.addColumna(str(i), "REAL")

		for i in range(0, numeroClases):
			instances.addClase(str(i))

		for line in iter(lambda: f.readline(), ''):
			tokens = self.privateLimpiaVacioTokens(re.split(self.delimiters, line))
			#print tokens
			if len(tokens) <= 0:
				break
			#instancia al estilo WEKA
			instance = Instance()
			#se anyaden las entradas del perceptron
			for i in range(0, numeroEntradas):
				#print filter(lambda x: x in string.printable, tokens[i])
				instance.addElement(tokens[i])

			#print tokens[numeroEntradas]
			instance.addElement(tokens[numeroEntradas])

			instances.addInstance(instance)

		f.close()
		return instances

	def privateLimpiaVacioTokens(self, tokens):
		lista = []
		for token in tokens:
			if token == '':
				pass
			else:
				lista.append(token)

		return lista