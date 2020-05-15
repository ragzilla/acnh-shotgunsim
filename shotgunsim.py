#! /usr/bin/python3

from data import turtle_layout, pairs_layout
import numpy as np

from flower import Flower
from field import Field
from pairbreeder import PairBreeder
from feeder import Feeder

def main():
	target = [ [2,2,0],[2,2,1],[2,2,2] ]
	genes  = [ [1,1,0],[1,2,0],[2,0,0],[2,1,0] ] # simulating t110 x t110
	probs  = [ 4/9,    2/9,    1/9,    2/9     ] # 25/12.5/6.25/12.5
	genemap = len(probs)

	for run in range(1):
		turtle = Field(turtle_layout)
		pairs  = Field(pairs_layout)
		pairer = PairBreeder(pairs)
		feeder = Feeder(genes, probs)
		for day in range(365):
			print("day",day,feeder.feed())

	return

if __name__ == "__main__":
    main()
