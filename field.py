#! /usr/bin/python3

class Field:
	layout = None
	matrix = None

	def __init__(self, configuration):
		self.layout = configuration
		return

	def place(self, flower1, flower2 = None):
		"""place 1-2 flowers in the layout from the feeder"""
		print("Field: add:", flower1, flower2)
		return

	def run(self):
		"""run the day"""
		return

	def __repr__(self):
		return str(self.layout)
