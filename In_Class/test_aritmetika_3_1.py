import unittest
import aritmetika_3 as aritmetika

class TestAritmetika(unittest.TestCase):
    
    def test_sudetis(self):
        self.assertEqual(15, aritmetika.sudetis(10,5))
        self.assertEqual(0, aritmetika.sudetis(-1,1))
        self.assertEqual(-2, aritmetika.sudetis(-1,-1))

    def test_atimtis(self):
        self.assertEqual(5, aritmetika.atimtis(10,5))
        self.assertEqual(-2, aritmetika.atimtis(-1,1))
        self.assertEqual(0, aritmetika.atimtis(-1,-1))

    def test_daugyba(self):
        self.assertEqual(50, aritmetika.daugyba(10,5))
        self.assertEqual(-1, aritmetika.daugyba(-1,1))
        self.assertEqual(1, aritmetika.daugyba(-1,-1))

    def test_dalyba(self):
        self.assertEqual(2, aritmetika.dalyba(10,5))
        self.assertEqual(-1, aritmetika.dalyba(-1,1))
        self.assertEqual(1, aritmetika.dalyba(-1,-1))
        self.assertEqual(2.5, aritmetika.dalyba(5, 2))

    
if __name__ == "__main__":
    unittest.main()