import random
import unittest

import numpy

from descriptiveStatistics import DescriptiveStatistics
from randomGeneration import RandomGenerator


class TestCases(unittest.TestCase):
	def setUp(self):
		self.testdata = RandomGenerator.range_list_seed(2502, 15, 0, 1000)
		self.testdata2 = RandomGenerator.range_list_seed(7974, 15, 0, 1000)

	def test_mean(self):
		self.assertAlmostEqual(495.93333333333334, DescriptiveStatistics.mean(self.testdata))

	def test_median(self):
		self.assertEqual(568, DescriptiveStatistics.median(self.testdata))

	def test_mode(self):
		self.assertEqual(146, DescriptiveStatistics.mode(self.testdata))

	def test_variance(self):
		self.assertAlmostEqual(83691.20952380952, DescriptiveStatistics.variance(self.testdata))

	def test_stdev(self):
		self.assertAlmostEqual(289.29433026557837, DescriptiveStatistics.stdev(self.testdata))

	def test_quartiles(self):
		self.assertEqual( (231, 568, 705) , DescriptiveStatistics.quartiles(self.testdata))

	def test_skewness(self):
		self.assertAlmostEqual(-0.057826500059548105, DescriptiveStatistics.skewness(self.testdata))

	def test_sampleCorrelation(self):
		self.assertAlmostEqual(-0.053507170783676304, DescriptiveStatistics.sampleCorrelation(self.testdata, self.testdata2))

	def test_populationCorrelation(self):
		self.assertAlmostEqual(-0.057329111553938904, DescriptiveStatistics.populationCorrelation(self.testdata, self.testdata2))

	def test_zscore(self):
		arr = DescriptiveStatistics.zscore(self.testdata)
		res = [
			-1.25206537, 0.70152872, 0.50473811, -1.44527797, 1.07721989, 0.74804286,
			-0.83343806, -0.45416888, 0.25785534, -1.5204162,  1.55309537, 1.47795714,
			-0.15003793, 0.28290141, -0.94793442
		 ]

		for i in range(len(res)):
			self.assertAlmostEqual(res[i], arr[i])

	def test_meanDev(self):
		self.assertAlmostEqual(246.0711111111111, DescriptiveStatistics.meanDev(self.testdata))
