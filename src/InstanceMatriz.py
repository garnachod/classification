class Instance(object):
	"""docstring for Instance"""
	def __init__(self):
		super(Instance, self).__init__()
		self.listaDatos = []
		self.instances = None
		self.bipVectorObjetivo = None
	
	def addElement(self, elemento):
		self.listaDatos.append(elemento)

	def setInstances(self, instances):
		self.instances = instances

	def getElementAtPos(self, pos):
		return self.listaDatos[pos]

	def setElementAtPos(self, elem, pos):
		self.listaDatos[pos] = elem

	def getAllElements(self):
		return self.listaDatos

	def getClase(self):
		longitud = len(self.listaDatos)
		return self.listaDatos[longitud - 1]

	def getBipolarVectorObjetivoSalida(self, clases):
		if self.bipVectorObjetivo == None:
			claseIn = self.getClase()
			self.bipVectorObjetivo = []
			for clase in clases:
				if clase == claseIn:
					self.bipVectorObjetivo.append(1.0)
				else:
					self.bipVectorObjetivo.append(-1.0)
	
		return self.bipVectorObjetivo


		