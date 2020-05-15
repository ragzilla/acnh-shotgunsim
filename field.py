#! /usr/bin/python3

class Field:
	name   = None
	layout = None
	matrix = None

	def __init__(self, name, configuration):
		self.name   = name
		self.layout = configuration
		self.x      = len(self.layout[0])
		self.y      = len(self.layout)
		self.matrix = [ [ None for i in range(self.x) ] for j in range(self.y) ] 
		print(self.name, self.matrix, self.y, self.x)
		return

	def place(self, flower1, flower2 = None):
		"""place 1-2 flowers in the layout from the feeder"""
		### find an open spot
		print("Field(\"{}\").place:".format(self.name), flower1, flower2)
		flowers = [flower1,]
		if flower2 != None:
			flowers.append(flower2)
		for y in range(self.y):
			if len(flowers) == 0:
				break
			for x in range(self.x):
				if self.layout[y][x] == 1 and self.matrix[y][x] == None:
					self.matrix[y][x] = flowers.pop()
				if len(flowers) == 0:
					break
		print(self.matrix)
		return

	def run(self):
		"""run the day"""
		return

	def __repr__(self):
		return str(self.layout)
