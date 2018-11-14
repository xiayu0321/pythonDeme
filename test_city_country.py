import unittest

from city_functions import city_country

class NameTestCase(unittest.TestCase):
	def test_city_country():
		c_c = city_country('ShangHai','China',2000)
		self.assertEqual(c_c,'ShangHai,China - 2000')