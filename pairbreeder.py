#! /usr/bin/python3

class PairBreeder:
	"""really more of a pair cloner"""
	flowers = None

	def __init__(self):
		self.flowers = []

	def place(self, flower):
		"""add a flower to the PairBreeder"""
		print("PairBreeder.place:", flower)
		self.flowers.append(flower)
		return

	def breed(self):
		"""breeds all flowers, if a pair results, return them to the caller"""
		retval = []
		delete = []
		for flower in self.flowers:
			new_flower = flower.breed()
			if new_flower:
				delete.append(flower)
				retval.append([flower, new_flower])
		for flower in delete:
			self.flowers.remove(flower)
		return retval