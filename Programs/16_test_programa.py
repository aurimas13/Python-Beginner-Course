# Python faile test_programa.py

import unittest
from programavienas import Skaiciavimai

class TestSkaiciavimai(unittest.TestCase):
    def setUp(self):
        self.objektas = Skaiciavimai()

    def test_sudetis(self):
        self.assertEqual(self.objektas.sudetis(5, 5), 10) 
        self.assertEqual(self.objektas.sudetis(-1, 1), 0)
        self.assertEqual(self.objektas.sudetis(0, 0), 0)

    def test_daugyba(self):
        self.assertEqual(self.objektas.daugyba(5, 5), 25) 
        self.assertEqual(self.objektas.daugyba(-1, 1), -1)
        self.assertEqual(self.objektas.daugyba(0, 5), 0)

    def test_dalyba(self):
        self.assertEqual(self.objektas.dalyba(10, 5), 2)
        self.assertEqual(self.objektas.dalyba(-1, 1), -1)
        self.assertEqual(self.objektas.dalyba(10, 0), "Klaida: dalinimas iš nulio negalimas")

if __name__ == '__main__':
    unittest.main()
