import unittest
from  listas_diccionarios import repetidos

class Testupper(unittest.TestCase):
    def test_1(self):
        list = repetidos([1,2,3])
        self.assertEqual(list, {1:1, 2:1, 3:1})

    def test_2(self):
        list = repetidos([1,1,2,3])
        self.assertEqual(list, {1:2, 2:1, 3:1})

    def test_3(self):
        list = repetidos([1,1,1,1,2,3])
        self.assertEqual(list, {1:4, 2:1, 3:1})

    def test_4(self):
        list = repetidos([1,1,1,1,2,2,3])
        self.assertEqual(list, {1:4, 2:2, 3:1})

if __name__ == '__main__':
    unittest.main()