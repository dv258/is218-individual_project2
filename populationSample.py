import math
import random

import numpy
import scipy.stats

from descriptiveStatistics import DescriptiveStatistics
from randomGeneration import RandomGenerator


class PopulationSampling:
	def __init__(self):
		pass

	@staticmethod
	def randomSampling(data, n):
		return random.sample(data, n)

	@staticmethod
	def systematicSampling(data, n):
		items = []
		k = len(data) // n

		idx = RandomGenerator.range(0, len(data))
		for c in range(n):
			items.append(data[idx])

			idx += k
			if idx >= len(data):
				idx -= len(data)

		return items

	@staticmethod
	def confidenceInterval(data, confidence):
		mean = DescriptiveStatistics.mean(data)
		se = scipy.stats.sem(data)
		i = se * PopulationSampling.tscore(len(data), confidence)
		return (mean, mean - i, mean + i)

	@staticmethod
	def marginOfError(data, confidence):
		cv = PopulationSampling.tscore(len(data), confidence)
		se = scipy.stats.sem(data)

		return cv * se

	@staticmethod
	def tscore(n, confidence):
		return scipy.stats.t.ppf(confidence, n - 1)
