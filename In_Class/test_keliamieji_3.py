import unittest
from keliamieji_3 import ar_keliamieji

class TestKeliamieji(unittest.TestCase):
    
    def test_ar_keliamieji(self):
        self.assertTrue(ar_keliamieji(2000))
        self.assertTrue(ar_keliamieji(2020))
        self.assertFalse(ar_keliamieji(2100))

if __name__ == "__main__":
    unittest.main()