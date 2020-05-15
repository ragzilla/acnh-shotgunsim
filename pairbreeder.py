#! /usr/bin/python3

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