#! /usr/bin/python3

import numpy as np

class Feeder:
	genemap  = None
	genepool = None
	probpool = None
	pitypool = None

	def __init__(self, genepool, probpool):
		self.genepool = genepool
		self.probpool = probpool
		self.genemap  = len(probpool)
		return

	def feed(self):
		return self.genepool[np.random.choice(self.genemap, None, True, self.probpool)]
