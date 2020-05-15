#! /usr/bin/python3

class PairBreeder:
	flowers = None

	def __init__(self):
		self.flowers = []

	def add(self, flower):
		"""add a flower to the PairBreeder"""
		print("PairBreeder: add:", flower)
		return

	def breed(self):
		"""breeds all flowers, if a pair results, return them to the caller"""
		return []