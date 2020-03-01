class StatsCalc:
	def __init__(self):
		self.result = None

	def randomSampling(self, data, n):
		self.result = PopulationSampling.randomSampling(data, n)
		return self.result

	def test_systematicSampling(self, data):
		self.result = PopulationSampling.systematicSampling(data, n)
		return self.result

	def test_confidenceInterval(self, data, confidence):
		self.result = PopulationSampling.confidenceInterval(data, confidence)
		return self.result

	def test_marginOfError(self, data, confidence):
		self.result = PopulationSampling.marginOfError(data, confidence)
		return self.result

	def test_mean(self, data):
		self.result = DescriptiveStatistics.mean(data)
		return self.result

	def test_median(self, data):
		self.result = DescriptiveStatistics.median(data)
		return self.result

	def test_mode(self, data):
		self.result = DescriptiveStatistics.mode(data)
		return self.result

	def test_variance(self, data):
		self.result = DescriptiveStatistics.variance(data)
		return self.result

	def test_stdev(self, data):
		self.result = DescriptiveStatistics.stdev(data)
		return self.result

	def test_quartiles(self, data):
		self.result = DescriptiveStatistics.quartiles(self.testdata)
		return self.result

	def test_skewness(self, data):
		self.result = DescriptiveStatistics.skewness(data)
		return self.result

	def test_sampleCorrelation(self, data1, data2):
		self.result = DescriptiveStatistics.sampleCorrelation(data1, data2)
		return self.result

	def test_populationCorrelation(self, data1, data2):
		self.result = DescriptiveStatistics.populationCorrelation(data, data2)
		return self.result

	def test_zscore(self, data):
		self.result = DescriptiveStatistics.zscore(data)
		return self.result

	def test_meanDev(self, data):
		self.result = DescriptiveStatistics.meanDev(data)
		return self.result
