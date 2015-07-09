import random

class Nodo(object):
	"""docstring for Nodo"""
	def __init__(self, palabra):
		super(Nodo, self).__init__()
		self.nodosConectados = {}
		self.palabra = palabra

	def setConexo(self, nodo):
		#peso = random.random() - 0.5
		peso = 0.1
		palabra = nodo.getPalabra()
		self.nodosConectados[palabra] = peso
		#peso = random.random() - 0.5
		peso = 0.1
		palabra = self.getPalabra()
		nodo.nodosConectados[palabra] = peso

	def isConexo(self, palabra):
		if palabra in self.nodosConectados:
			return True
		else:
			return False

	def getPalabra(self):
		return self.palabra

	def getPeso(self, palabra):
		peso = self.nodosConectados[palabra]
		return peso

	def sumaAlPeso(self, palabra, cantidad):
		self.nodosConectados[palabra] += cantidad

	def randomizaTodosPesos(self):
		for palabra in self.nodosConectados:
			self.nodosConectados[palabra] += random.random() - 0.5

	def randomizaProporPesos(self, probabilidad, alpha):
		for palabra in self.nodosConectados:
			if random.random() <= probabilidad:
				self.nodosConectados[palabra] += (random.random() - 0.5) * alpha

	def duplica(self):
		duplicado = Nodo(self.palabra)
		for palabra in self.nodosConectados:
			duplicado.nodosConectados[palabra] = float(self.nodosConectados[palabra])

		return duplicado
