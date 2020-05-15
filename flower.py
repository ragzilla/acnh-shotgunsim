#! /usr/bin/python3

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

	def breed(self, partner):
		partner_genes = partner.get_genes()
		return

	def make_invalid(self):
		return

	def is_valid(self):
		return

	def reset_day(self):
		return
