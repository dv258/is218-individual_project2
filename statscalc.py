from descriptivestatistics import DescriptiveStatistics
from populationsampling import PopulationSampling


class StatsCalc:
	def __init__(self):
		self.result = None

	def simpleRandomSampling(self, data, n):
		self.result = PopulationSampling.simpleRandomSampling(data, n)
		return self.result

	def systematicSampling(self, data):
		self.result = PopulationSampling.systematicSampling(data, n)
		return self.result

	def confidenceInterval(self, data, confidence):
		self.result = PopulationSampling.confidenceInterval(data, confidence)
		return self.result

	def marginOfError(self, pstdev, n, confidenceLevel)
		self.result = PopulationSampling.marginOfError(pstdev, n, confidenceLevel)
		return self.result

	def cochranSampleSize(self, p, confidenceLevel, precision):
		self.result = PopulationSampling.cochranSampleSize(p, confidenceInterval, precision)
		return self.result

	def findSampleSize(self, stdev, confidenceLevel, precision):
		self.result = PopulationSampling.findSampleSize(stdev, confidenceInterval, precision)
		return self.result

	def mean(self, data):
		self.result = DescriptiveStatistics.mean(data)
		return self.result

	def median(self, data):
		self.result = DescriptiveStatistics.median(data)
		return self.result

	def mode(self, data):
		self.result = DescriptiveStatistics.mode(data)
		return self.result

	def stdev(self, data):
		self.result = DescriptiveStatistics.stdev(data)
		return self.result

	def variance(self, data):
		self.result = DescriptiveStatistics.variance(data)
		return self.result

	def quartiles(self, data):
		self.result = DescriptiveStatistics.quartiles(self.testdata)
		return self.result

	def skewness(self, data):
		self.result = DescriptiveStatistics.skewness(data)
		return self.result

	def zscore(self, value, mean, stdev):
		self.result = DescriptiveStatistics.zscore(value, mean, stdev)
		return self.result

	def meanDeviation(self, data):
		self.result = DescriptiveStatistics.meanDeviation(data)
		return self.result

	def sampleCorrelation(self, data1, data2):
		self.result = DescriptiveStatistics.sampleCorrelation(data1, data2)
		return self.result

	def populationCorrelation(self, data1, data2):
		self.result = DescriptiveStatistics.populationCorrelation(data, data2)
		return self.result
