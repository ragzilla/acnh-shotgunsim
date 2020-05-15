#! /usr/bin/python3

import numpy as np

baserepro =  [ 0.05, 0.05, 0.05, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, \
               0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, ]
bonusrepro = [ 0, 0.2, 0.3, 0.45, 0.6, 0.75 ]

class Feeder:
	genemap  = None
	genepool = None
	probpool = None
	pitypool = None

	def __init__(self, genepool, probpool, visit = 0, pairs = 8):
		self.genepool = genepool
		self.probpool = probpool
		self.genemap  = len(probpool)
		self.visit    = visit
		self.pitypool = [0] * pairs
		return

	def feed(self):
		retval = []
		for i in range(len(self.pitypool)):
			if (baserepro[self.pitypool[i]] + bonusrepro[self.visit]) > np.random.random():
				# success!
				self.pitypool[i] = 0
				retval.append(self.genepool[np.random.choice(self.genemap, None, True, self.probpool)])
			else:
				self.pitypool[i] += 1
		return retval
