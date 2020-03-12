import math
import random

import scipy.stats

from descriptivestatistics import DescriptiveStatistics


class PopulationSampling:
	def __init__(self):
		pass

	@staticmethod
	def simpleRandomSampling(data, n):
		sample = []

		for i in range(n):
			r = random.randrange(0, len(data))
			sample.append(r)

			#without replacement
			data = data[:r] + data[r + 1:]

		return sample

	@staticmethod
	def systematicSampling(data, n):
		sample = []
		k = len(data) // n

		idx = random.randrange(0, len(data))
		for i in range(n):
			sample.append(data[idx])

			idx += k
			if idx >= len(data):
				idx -= len(data)

		return sample

	@staticmethod
	def confidenceInterval(data, confidence):
		mean = DescriptiveStatistics.mean(data)
		se = scipy.stats.sem(data)
		i = se * PopulationSampling.tscore(len(data), confidence)
		return [mean, mean - i, mean + i]

	@staticmethod
	def marginOfError(pstdev, n, confidenceLevel):
		zscore = scipy.stats.norm.ppf(confidenceLevel)
		return zscore * pstdev / math.sqrt(n)

	@staticmethod
	def cochranSampleSize(p, confidenceLevel, precision):
		zscore = scipy.stats.norm.ppf(confidenceLevel + (1 - confidenceLevel) / 2)
		return math.ceil((zscore ** 2) * p * (1 - p) / (precision ** 2))

	@staticmethod
	def findSampleSize(stdev, confidenceLevel, precision):
		zscore = scipy.stats.norm.ppf(confidenceLevel + (1 - confidenceLevel) / 2)
		return math.ceil((zscore * stdev / precision) ** 2)

	@staticmethod
	def tscore(n, confidence):
		return scipy.stats.t.ppf(confidence, n - 1)
