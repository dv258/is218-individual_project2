import statistics

import numpy
import scipy.stats


class DescriptiveStatistics:
	def __init__(self):
		pass

	@staticmethod
	def mean(data):
		return sum(data) / len(data)

	@staticmethod
	def median(data):
		dataSorted = data[:]
		dataSorted.sort()

		return DescriptiveStatistics._median(dataSorted)[0]

	@staticmethod
	def mode(data):
		dcount = {}
		largest = data[0]

		for x in data:
			if x not in dcount:
				dcount[x] = 0
			dcount[x] += 1

			if dcount[x] > dcount[largest]:
				largest = x

		return largest

	@staticmethod
	def variance(data, xbar=None):
		return statistics.variance(data, xbar)

	@staticmethod
	def pvariance(data, xbar=None):
		return statistics.pvariance(data, xbar)

	@staticmethod
	def covariance(data1, data2):
		mean1 = DescriptiveStatistics.mean(data1)
		mean2 = DescriptiveStatistics.mean(data2)
		total = 0

		for d1, d2 in zip(data1, data2):
			total += (d1 - mean1) * (d2 - mean2)
		return 1 / (len(data1) - 1) * total

	@staticmethod
	def stdev(data, xbar=None):
		return statistics.stdev(data, xbar)

	@staticmethod
	def pstdev(data, xbar=None):
		return statistics.pstdev(data, xbar)

	@staticmethod
	def quartiles(data):
		dataSorted = data[:]
		dataSorted.sort()

		secondQuartile, pos = DescriptiveStatistics._median(dataSorted)

		lowerhalf = dataSorted[:pos[0]]
		upperhalf = dataSorted[pos[1]:]

		firstQuartile, _ = DescriptiveStatistics._median(lowerhalf)
		thirdQuartile, _ = DescriptiveStatistics._median(upperhalf)

		return ( firstQuartile, secondQuartile, thirdQuartile )

	@staticmethod
	def skewness(data):
		return scipy.stats.skew(data)

	@staticmethod
	def sampleCorrelation(data1, data2):
		return scipy.stats.pearsonr(data1, data2)[0]

	@staticmethod
	def populationCorrelation(data1, data2):
		return DescriptiveStatistics.covariance(data1, data2) / (DescriptiveStatistics.pstdev(data1) * DescriptiveStatistics.pstdev(data2))

	@staticmethod
	def zscore(data):
		return scipy.stats.zscore(data)

	@staticmethod
	def meanDev(data):
		lst = []
		dmean = DescriptiveStatistics.mean(data)

		for d in data:
			lst.append(abs(d - dmean))

		return DescriptiveStatistics.mean(lst)

	'''data should be a sorted list'''
	@staticmethod
	def _median(data):
		mid = len(data) // 2
		if len(data) % 2 == 1:
			return ( data[mid], ( mid, mid + 1 ) )
		return ( (data[mid - 1] + data[mid]) / 2, ( mid, mid ) )
