import random
import unittest

from populationsampling import PopulationSampling
from randomgenerator import RandomGenerator


class TestCases(unittest.TestCase):
	def setUp(self):
		self.testdata = RandomGenerator.range_list_seed(2502, 15, 0, 1000)

	def test_simpleRandomSampling(self):
		random.seed(23)
		self.assertEqual([14, 12, 4, 1], PopulationSampling.simpleRandomSampling(self.testdata, 4))

	def test_systematicSampling(self):
		random.seed(23)
		self.assertEqual([231, 637, 705, 568], PopulationSampling.systematicSampling(self.testdata, 4))

	def test_confidenceInterval(self):
		r = PopulationSampling.confidenceInterval(self.testdata, 0.95)
		self.assertAlmostEqual(495.93333333, r[0])
		self.assertAlmostEqual(364.37143632, r[1])
		self.assertAlmostEqual(627.49523034, r[2])

	def test_marginOfError(self):
		self.assertAlmostEqual(0.02193138, PopulationSampling.marginOfError(0.4, 900, 0.95))

	def test_cochranSampleSize(self):
		self.assertAlmostEqual(385, PopulationSampling.cochranSampleSize(0.5, 0.95, 0.05))

	def test_findSampleSize(self):
		self.assertAlmostEqual(224, PopulationSampling.findSampleSize(2.9, 0.99, 0.5))
