#! /usr/bin/python3

from itertools import product
from numpy.random import shuffle
from sys import exit

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
		# print(self.name, self.matrix, self.y, self.x)
		return

	def place(self, flower1, flower2 = None):
		"""place 1-2 flowers in the layout from the feeder"""
		### find an open spot
		# print("Field(\"{}\").place:".format(self.name), flower1, flower2)
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
		# print(self.matrix)
		return

	def neighbors(self, x, y):
		cell = (x,y)
		for c in product(*(range(n-1, n+2) for n in cell)):
			if c != cell and (0 <= c[0] < self.x) and (0 <= c[1] < self.y): #  for n in c)
				yield c

	def run(self):
		"""reset the plants, run the day"""
		cull = [] # grid locations to cull and return when we're done
		harvest = []
		flowerstobreed = []
		for y in range(self.y):
			for x in range (self.x):
				if self.matrix[y][x] != None:
					self.matrix[y][x].reset_day()
					flowerstobreed.append((x,y))
		# randomize the list
		shuffle(flowerstobreed)
		# print("run/", self.name, "/", flowerstobreed)
		# run through them, one by one
		for grid in flowerstobreed:
			x = grid[0]
			y = grid[1]
			parent = self.matrix[y][x]
			# print("breeding at",grid,parent)
			if not parent.is_valid():
				continue # already bred today, skip
			opentile = None
			partner  = None
			neighbors = list(self.neighbors(x, y))
			shuffle(neighbors)
			for neighbor in neighbors:
				nx = neighbor[0]
				ny = neighbor[1]
				n = self.matrix[ny][nx]
				if n == None:
					if opentile == None:
						opentile = neighbor
				elif partner == None and n.is_valid():
					partner = n
				if opentile != None and partner != None:
					break
			if opentile == None:
				continue ## we can't breed without a target tile
			new_flower = parent.breed(partner)
			if new_flower != None:
				# print("flower",parent,"breeding with",partner,"into tile",opentile,"new:",new_flower)
				cull.append(opentile)
				harvest.append(new_flower)
				nx = opentile[0]
				ny = opentile[1]
				self.matrix[ny][nx] = new_flower
		for opentile in cull:
			nx = opentile[0]
			ny = opentile[1]
			self.matrix[ny][nx] = None
		return harvest

	def __repr__(self):
		return str(self.layout)
