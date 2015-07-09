# -*- coding: utf-8 -*-
from heapq import heappush, heappop
from Instance import Instance
from Instances import Instances
from operator import add,mul
from textblob import TextBlob
from Nodo import Nodo
from nltk.stem.lancaster import LancasterStemmer
import random
import math

class IndividuoRedPalabras(object):
	"""docstring for Clasificador"""
	def __init__(self):
		super(IndividuoRedPalabras, self).__init__()
		self.nodosPorClase = {}
		self.clases = []
		self.probMutacion = 0.5
		self.alpha = 0.1
		self.stopWords = "a|about|above|after|again|against|all|am|an|and|any|are|aren't|as|at|be|because|been|before|being|below|between|both|but|by|can't|cannot|could|couldn't|did|didn't|do|does|doesn't|doing|don't|down|during|each|few|for|from|further|had|hadn't|has|hasn't|have|haven't|having|he|he'd|he'll|he's|her|here|here's|hers|herself|him|himself|his|how|how's|i|i'd|i'll|i'm|i've|if|in|into|is|isn't|it|it's|its|itself|let's|me|more|most|mustn't|my|myself|no|nor|not|of|off|on|once|only|or|other|ought|our|ours|ourselves|out|over|own|same|shan't|she|she'd|she'll|she's|should|shouldn't|so|some|such|than|that|that's|the|their|theirs|them|themselves|then|there|there's|these|they|they'd|they'll|they're|they've|this|those|through|to|too|under|until|up|very|was|wasn't|we|we'd|we'll|we're|we've|were|weren't|what|what's|when|when's|where|where's|which|while|who|who's|whom|why|why's|with|won't|would|wouldn't|you|you'd|you'll|you're|you've|your|yours|yourself|yourselves"
		self.st = LancasterStemmer()

	def mutacion(self):
		for clase in self.nodosPorClase:
			for palabra in self.nodosPorClase[clase]:
				if random.random() <= self.probMutacion:
					self.nodosPorClase[clase][palabra].randomizaProporPesos(self.probMutacion, self.alpha)

	def duplica(self):
		duplicado = IndividuoRedPalabras()
		duplicado.clases = list(self.clases)

		for clase in self.nodosPorClase:
			duplicado.nodosPorClase[clase] = {}
			for palabra in self.nodosPorClase[clase]:
				duplicado.nodosPorClase[clase][palabra] = self.nodosPorClase[clase][palabra].duplica()

		return duplicado

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
				if palabra in self.stopWords:
					continue
				palabra = self.st.stem(palabra)
				if palabra in self.nodosPorClase[clase]:
					if nodoAnterior is None:
						nodoAnterior = self.nodosPorClase[clase][palabra]
					else:
						nodo = self.nodosPorClase[clase][palabra]
						if nodoAnterior.isConexo(palabra):
							nodoAnterior.sumaAlPeso(palabra, 0.15)
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

		for clase in self.nodosPorClase:
			for palabra in self.nodosPorClase[clase]:
				self.nodosPorClase[clase][palabra].randomizaTodosPesos()


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
				palabra = palabra.lower()
				if palabra in self.stopWords:
					continue
				palabra = self.st.stem(palabra)
				if palabra in self.nodosPorClase[clase]:
					if nodoAnterior is None:
						nodoAnterior = self.nodosPorClase[clase][palabra]
					else:
						if nodoAnterior.isConexo(palabra):
							peso = nodoAnterior.getPeso(palabra)
							pesoClase[clase] += peso
						else:
							#por ahora nada, pero se debería aplicar dikstra
							pesoClase[clase] -= 0.1
				else:
					pesoClase[clase] -= 0.2

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

