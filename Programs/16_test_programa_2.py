# test_programa.py

import unittest
from programa import ManoKlase

class TestManoKlase(unittest.TestCase):
    def setUp(self):
        # Inicijuojame klasės objektą, kurį naudosime testuose
        self.objektas = ManoKlase()

    def test_sudetis(self):
        # Patikriname ar sudėties funkcija veikia teisingai
        self.assertEqual(self.objektas.sudetis(2, 2), 4)
        self.assertEqual(self.objektas.sudetis(-1, 1), 0)
        self.assertEqual(self.objektas.sudetis(0, 0), 0)

    def test_daugyba(self):
        # Patikriname ar daugybos funkcija veikia teisingai
        self.assertEqual(self.objektas.daugyba(2, 3), 6)
        self.assertEqual(self.objektas.daugyba(-1, 1), -1)
        self.assertEqual(self.objektas.daugyba(0, 5), 0)

    def test_dalyba(self):
        # Patikriname ar dalybos funkcija veikia teisingai
        self.assertEqual(self.objektas.dalyba(10, 5), 2)
        self.assertEqual(self.objektas.dalyba(-1, 1), -1)
        self.assertEqual(self.objektas.dalyba(10, 2), 5)

if __name__ == "__main__":
    unittest.main()
