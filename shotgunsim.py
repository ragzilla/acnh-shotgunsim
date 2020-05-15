#! /usr/bin/python3

from data import turtle_layout, pairs_layout
import numpy as np

class Flower:
	genes = None
	pity  = 0
	visit = 0

	def __init__(self, genes, visit):
		self.genes = genes
		self.pity  = 0
		self.visit = visit

	def breed(self, partner):
		return

class Field:
	layout = None
	matrix = None

	def __init__(self, configuration):
		self.layout = configuration
		return

	def __repr__(self):
		return str(self.layout)

class PairBreeder:
	flowers = None
	pairs   = None

	def __init__(self, pairs):
		self.flowers = []
		self.pairs   = pairs

	def add(self, flower):
		"""add a flower to the PairBreeder"""
		print("adding:", flower)
		return

	def breed(self):
		"""breeds all flowers, if a pair results, put them into self.pairs"""
		return

class Feeder:
	genepool = None
	probpool = None

	def __init__(self, genepool, probpool):
		return

def main():
	genes = [ [1,1,0],[1,2,0],[2,0,0],[2,1,0] ] # simulating t110 x t110
	probs = [ 4/9,      2/9,      1/9,      2/9       ] # 25/12.5/6.25/12.5
	genemap = len(probs)
	turtle = Field(turtle_layout)
	pairs  = Field(pairs_layout)
	pairer = PairBreeder(pairs)
	feeder = Feeder(genes, probs)

	for run in range(1000):
		flower = genes[np.random.choice(genemap, None, True, probs)]
		print(flower)

	return

if __name__ == "__main__":
    main()
