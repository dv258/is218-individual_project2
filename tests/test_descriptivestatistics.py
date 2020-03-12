import random
import unittest

import numpy

from descriptivestatistics import DescriptiveStatistics
from randomgenerator import RandomGenerator


class TestCases(unittest.TestCase):
	def setUp(self):
		self.testdata = RandomGenerator.range_list_seed(2502, 15, 0, 1000)
		self.testdata2 = RandomGenerator.range_list_seed(7974, 15, 0, 1000)

	def test_mean(self):
		self.assertAlmostEqual(495.93333333, DescriptiveStatistics.mean(self.testdata))

	def test_median(self):
		self.assertEqual(568, DescriptiveStatistics.median(self.testdata))

	def test_mode(self):
		self.assertEqual([], DescriptiveStatistics.mode(self.testdata))

	def test_variance(self):
		self.assertAlmostEqual(83691.20952380, DescriptiveStatistics.variance(self.testdata))

	def test_stdev(self):
		self.assertAlmostEqual(289.29433026, DescriptiveStatistics.stdev(self.testdata))

	def test_quartiles(self):
		self.assertEqual( [231, 568, 705] , DescriptiveStatistics.quartiles(self.testdata))

	def test_skewness(self):
		self.assertAlmostEqual(-0.74733576, DescriptiveStatistics.skewness(self.testdata))

	def test_sampleCorrelation(self):
		self.assertAlmostEqual(-0.05350717, DescriptiveStatistics.sampleCorrelation(self.testdata, self.testdata2))

	def test_populationCorrelation(self):
		self.assertAlmostEqual(-0.05350717, DescriptiveStatistics.populationCorrelation(self.testdata, self.testdata2))

	def test_zscore(self):
		value = 1100
		mean = 1026
		stdev = 209
		self.assertAlmostEqual(0.35406698, DescriptiveStatistics.zscore(value, mean, stdev))

	def test_meanDeviation(self):
		self.assertAlmostEqual(246.07111111, DescriptiveStatistics.meanDeviation(self.testdata))
