#! /usr/bin/python3

from data import turtle_layout, pairs_layout
import numpy as np

from flower import Flower
from field import Field
from pairbreeder import PairBreeder
from feeder import Feeder

def simulate(in_runs, in_pairs, in_visitors):
	target = [ [2,2,0],[2,2,1],[2,2,2] ]
	genes  = [ [1,1,0],[1,2,0],[2,0,0],[2,1,0] ] # simulating t110 x t110
	probs  = [ 4/9,    2/9,    1/9,    2/9     ] # 25/12.5/6.25/12.5
	genemap = len(probs)
	pairs_results = []
	turtle_results = []

	for run in range(in_runs):
		turtle_day = -1
		pairs_day = -1
		turtle = Field("turtle", turtle_layout)
		pairs  = Field("pairs", pairs_layout)
		pairer = PairBreeder()
		feeder = Feeder(genes, probs, visit=in_visitors, pairs=in_pairs)
		for day in range(1, 365):
			# get the days flowers
			feed = feeder.feed()
			# print("day",day,feed)

			# check for output from the pairer, put them into the pairs field
			for new_pair in pairer.breed():
				pairs.place(new_pair[0], new_pair[1])

			# add the day's feed into the pairer and the turtle
			for new_flower in feed:
				pairer.place(new_flower)
				turtle.place(new_flower)

			# everything above this point technically "runs" the day before
			# run the fields
			if pairs_day == -1:
				harvest  = pairs.run()
				# print("pairs:",  pairs_harvest)
				for flower in harvest:
					if flower.get_genes() in target:
						pairs_day = day
			if turtle_day == -1:
				harvest = turtle.run()
				# print("turtle:", turtle_harvest)
				for flower in harvest:
					if flower.get_genes() in target:
						turtle_day = day

			# break out if they both finish
			if turtle_day != -1 and pairs_day != -1:
				break
		if turtle_day != -1 and pairs_day != -1:
			# print("run", run, "ended on day", day, "turtle", turtle_day, "pairs", pairs_day)
			pairs_results.append(pairs_day)
			turtle_results.append(turtle_day)

	print("{}\t{}\tpairs\t{}\t{}\t{}\t{}\t{}".format(in_visitors, in_pairs, np.amin(pairs_results), np.amax(pairs_results), np.mean(pairs_results), np.median(pairs_results), np.percentile(pairs_results, 95)))
	print("{}\t{}\tturtle\t{}\t{}\t{}\t{}\t{}".format(in_visitors, in_pairs, np.amin(turtle_results), np.amax(turtle_results), np.mean(turtle_results), np.median(turtle_results), np.percentile(turtle_results, 95)))
	return

if __name__ == "__main__":
	print("visit\tfeed\tlayout\tmin\tmax\tmean\tmedian\t95th")	
	for visitors in (0, 1, 3, 5):
		for pairs in (1, 2, 4, 8, 16):
			simulate(10000, pairs, visitors)
