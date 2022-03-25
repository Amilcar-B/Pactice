import unittest
from src.calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        cal = Calculator()
        result = cal.add(2, 2)
        self.assertEquals(4, result)

    def test_validate_age(self):
        cal = Calculator()
        result = cal.valid_age(1)
        self.assertTrue(result)

    #def test_validate_invalid_age(self):
    #    cal = Calculator()
    #    result = cal.valid_age(-5)
    #    self.assertFalse(result)

    def test_max(self):
        cal = Calculator()
        result = cal.max(8, 15, 3)
        self.assertEquals(15, result)

    def test_isVocal(self):
        cal = Calculator()
        result = cal.isVocal('8')
        self.assertEquals('numero',result)

    def test_inversa(self):
        cal = Calculator()
        result = cal.inversa('AT16 Python')
        self.assertEquals('nohtyP 61TA',result)

    def test_palindromo(self):
        cal = Calculator()
        result = cal.palindromo('ana')
        self.assertTrue(result)

    def test_numeros(self):
        val = [1, 5, -10, 8, 2, 60, 4, 9]
        cal = Calculator()
        result = cal.numeros(val)
        self.assertEquals([60, -10, 9.875], result)

    def test_pais(self):
        p = ['chile', 'argentina', 'bolivia', 'canada', 'china', 'mexico','estados unidos', 'uruguay', 'venezuela']
        cal = Calculator()
        result = cal.pais(p)
        self.assertEquals(6, result)

    def test_binary(self):
        cal = Calculator()
        result = cal.binary(10)
        self.assertEquals('0b1010',result)

    def test_cantidad_caracteres(self):
        cadena = 'hola como estas'
        cal = Calculator()
        result = cal.cant(cadena)
        self.assertEquals(15, result)

