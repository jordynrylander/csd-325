# Jordyn Rylander
# Module 7.2 Assignment
# Unit tests for the city_country function.

import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_location = city_country("santiago", "chile")
        self.assertEqual(formatted_location, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()