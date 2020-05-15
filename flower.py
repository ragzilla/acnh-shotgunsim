#! /usr/bin/python3

import numpy as np
from data import baserepro, bonusrepro

class Flower:
	genes = None
	pity  = 0
	visit = 0
	invalid = False

	def __init__(self, genes, visit):
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
		if partner != None:
			### breed
			partner_genes = partner.get_genes()
			### make partner invalid?
			print("I NEED A PARTNER")
		else:
			### self clone
			new_flower = Flower(self.genes, self.visit)
		self.pity = 0
		return new_flower

	def make_invalid(self):
		self.invalid = True
		self.pity    = 0
		return

	def is_valid(self):
		return

	def reset_day(self):
		self.invalid = False
		return
