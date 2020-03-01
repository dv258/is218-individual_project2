import unittest

from randomGeneration import RandomGenerator


class TestCases(unittest.TestCase):
	def setUp(self):
		pass

	def test_range_seed(self):
		self.assertEqual(66, RandomGenerator.range_seed(17, 0, 100))

	def test_range_list_seed(self):
		self.assertEqual([66, 53, 38, 46, 37], RandomGenerator.range_list_seed(17, 5, 0, 100))

	def test_fromlist_seed(self):
		self.assertEqual(8, RandomGenerator.fromlist_seed(17, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

	def test_fromlist_multiple_seed(self):
		self.assertEqual([8, 6, 4, 5], RandomGenerator.fromlist_multiple_seed(17, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
