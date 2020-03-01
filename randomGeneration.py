import random


class RandomGenerator:
	def __init__(self):
		pass

	"""returns a random number in [nmin, nmax)"""
	@staticmethod
	def range(nmin, nmax):
		if type(nmin) == int and type(nmax) == int:
			return random.randrange(nmin, nmax)
		return random.random() * (nmax - nmin) + nmin

	@staticmethod
	def range_seed(seed, nmin, nmax):
		random.seed(seed)
		return RandomGenerator.range(nmin, nmax)

	@staticmethod
	def range_list_seed(seed, n, nmin, nmax):
		items = []

		random.seed(seed)
		for i in range(n):
			items.append(RandomGenerator.range(nmin, nmax))

		return items

	@staticmethod
	def fromlist(data):
		return data[RandomGenerator.range(0, len(data))]

	@staticmethod
	def fromlist_seed(seed, data):
		random.seed(seed)
		return RandomGenerator.fromlist(data)

	@staticmethod
	def fromlist_multiple(data, n):
		items = []

		for i in range(n):
			items.append(RandomGenerator.fromlist(data))

		return items

	@staticmethod
	def fromlist_multiple_seed(seed, data, n):
		random.seed(seed)
		return RandomGenerator.fromlist_multiple(data, n)

