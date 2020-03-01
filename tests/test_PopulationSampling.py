import random
import unittest

from populationSample import PopulationSampling
from randomGeneration import RandomGenerator


class TestCases(unittest.TestCase):
	def setUp(self):
		self.testdata = RandomGenerator.range_list_seed(2502, 15, 0, 1000)

	def test_randomSampling(self):
		random.seed(23)
		self.assertEqual([231, 454, 797, 692], PopulationSampling.randomSampling(self.testdata, 4))

	def test_systematicSampling(self):
		random.seed(23)
		self.assertEqual([231, 637, 705, 568], PopulationSampling.systematicSampling(self.testdata, 4))

	def test_confidenceInterval(self):
		r = PopulationSampling.confidenceInterval(self.testdata, 0.95)
		self.assertAlmostEqual(495.93333333333334, r[0])
		self.assertAlmostEqual(364.37143632235825, r[1])
		self.assertAlmostEqual(627.49523034430842, r[2])

	def test_marginOfError(self):
		self.assertAlmostEqual(131.56189701097509, PopulationSampling.marginOfError(self.testdata, 0.95))

