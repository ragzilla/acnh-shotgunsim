#! /usr/bin/python3

import numpy as np
from data import baserepro, bonusrepro, punnett_square

class Flower:
	genes = None
	pity  = 0
	visit = 0
	invalid = False

	def __init__(self, genes, visit = 0):
		self.genes = genes
		self.pity  = 0
		self.visit = visit
		self.invalid = False

	def __repr__(self):
		return "Flower({}, visit={})".format(str(self.genes), self.visit)

	def get_genes(self):
		return self.genes

	def breed(self, partner = None):
		new_flower = None
		### check to breed, return early, inverted logic from feeder for early return
		if (baserepro[self.pity] + bonusrepro[self.visit]) < np.random.random():
			### fail
			self.pity += 1
			return None
		self.make_invalid()
		if partner != None:
			### breed
			partner.make_invalid()
			partner_genes = partner.get_genes()
			new_genes = [ 0 ] * len(self.genes)
			for gIdx in range(len(self.genes)):
				new_genes[gIdx] = np.random.choice( punnett_square[self.genes[gIdx]][partner_genes[gIdx]] )
			new_flower = Flower(new_genes, self.visit)
		else:
			### self clone
			new_flower = Flower(self.genes, self.visit)
		return new_flower

	def make_invalid(self):
		self.invalid = True
		self.pity    = 0
		return

	def is_valid(self):
		return self.invalid == False

	def reset_day(self):
		self.invalid = False
		return
