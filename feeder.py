#! /usr/bin/python3

import numpy as np

from data import baserepro, bonusrepro
from flower import Flower

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
				retval.append(Flower(self.genepool[np.random.choice(self.genemap, None, True, self.probpool)], self.visit))
			else:
				self.pitypool[i] += 1
		return retval
