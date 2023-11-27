import unittest

class TestCalc(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(5, 3), 8)        
        self.assertEqual(sumar(-1, -1),-2)
        self.assertEqual(sumar(-1, 1), 0)

    def test_restar(self):
        self.assertEqual(restar(-1, -1),0)
        self.assertEqual(restar(10, 5), 5)
        self.assertEqual(restar(-1, 1), -2)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 7), 21)
        self.assertEqual(multiplicar(-1 , -1), 1)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(0, 10), 0)

    def test_dividir(self):
        self.assertEqual(dividir(10, 5), 2)
        self.assertEqual(dividir(-1, -1), 1)
        self.assertEqual(dividir(-1, 1), -1)

        self.assertRaises(ValueError, dividir, 10, 0)



