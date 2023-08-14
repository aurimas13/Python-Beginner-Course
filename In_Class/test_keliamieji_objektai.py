import unittest
from keliamieji_objektai import Keliamieji

class TestKeliamieji(unittest.TestCase):
    
    def test_tikrinti(self):
        objektas = Keliamieji()
        self.assertTrue(objektas.tikrinti(2000))
        self.assertTrue(objektas.tikrinti(2020))
        self.assertFalse(objektas.tikrinti(2100))

    def test_diapazonas(self):
        objektas = Keliamieji()
        rezultatas = objektas.diapazonas(1980, 2000)
        lukestis = [1980, 1984, 1988, 1992, 1996]
        self.assertEqual(lukestis, rezultatas)

if __name__ == "__main__":
    unittest.main()