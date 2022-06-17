
import unittest
from src.calculator import Calculator, DivisionByZeroError

class TestCalculator(unittest.TestCase):
    def test_add_zeroes(self):
        calc = Calculator(0,0)
        result = calc.add()
        self.assertEqual(result, 0, "sum between zeros failing")
    
    def test_add__positive_integers(self):
        calc = Calculator(6, 4)
        EXPECTED = 10
        result = calc.add()
        self.assertEqual(result, EXPECTED,
         f'sum between positive integers expected: {EXPECTED}, but got: {result}')
    
    def test_add_mixed_integers(self):
        calc = Calculator(6, -4)
        EXPECTED = 2
        result = calc.add()
        self.assertEqual(result, EXPECTED,
         f'sum between mixed integers expected: {EXPECTED}, but got: {result}')

    def test_add_negative_integers(self):
        calc = Calculator(-6, -4)
        EXPECTED = -10
        result = calc.add()
        self.assertEqual(result, EXPECTED,
         f'sum between negative integers expected: {EXPECTED}, but got: {result}')
    
    def test_subtract_zeroes(self):
        calc = Calculator(0,0)
        result = calc.subtract()
        self.assertEqual(result, 0, "subtraction between zeros failing")
    
    def test_subtract__positive_integers(self):
        calc = Calculator(6, 4)
        EXPECTED = 2
        result = calc.subtract()
        self.assertEqual(result, EXPECTED,
         f'subtraction between positive integers expected: {EXPECTED}, but got: {result}')
    
    def test_subtract_mixed_integers(self):
        calc = Calculator(6, -4)
        EXPECTED = 10
        result = calc.subtract()
        self.assertEqual(result, EXPECTED,
         f'subtraction between mixed integers expected: {EXPECTED}, but got: {result}')

    def test_subtract_negative_integers(self):
        calc = Calculator(-6, -4)
        EXPECTED = -2
        result = calc.subtract()
        self.assertEqual(result, EXPECTED,
         f'subtraction between negative integers expected: {EXPECTED}, but got: {result}')
    
    def test_multiply_zeroes(self):
        calc = Calculator(0,0)
        result = calc.multiply()
        self.assertEqual(result, 0, "multiplication between zeros failing")
    
    def test_multiply__positive_integers(self):
        calc = Calculator(6, 4)
        EXPECTED = 24
        result = calc.multiply()
        self.assertEqual(result, EXPECTED,
         f'multiplication between positive integers expected: {EXPECTED}, but got: {result}')
    
    def test_multiply_mixed_integers(self):
        calc = Calculator(6, -4)
        EXPECTED = -24
        result = calc.multiply()
        self.assertEqual(result, EXPECTED,
         f'multiplication between mixed integers expected: {EXPECTED}, but got: {result}')

    def test_multiply_negative_integers(self):
        calc = Calculator(-6, -4)
        EXPECTED = 24
        result = calc.multiply()
        self.assertEqual(result, EXPECTED,
         f'multiplication between negative integers expected: {EXPECTED}, but got: {result}')

    def test_divide_zeroes(self):
        calc = Calculator(0,0)
        self.assertRaises(DivisionByZeroError, calc.divide)
    
    def test_divide__positive_integers(self):
        calc = Calculator(6, 3)
        EXPECTED = 2
        result = calc.divide()
        self.assertEqual(result, EXPECTED,
         f'division between positive integers expected: {EXPECTED}, but got: {result}')
    
    def test_divide_mixed_integers(self):
        calc = Calculator(6, -3)
        EXPECTED = -2
        result = calc.divide()
        self.assertEqual(result, EXPECTED,
         f'division between mixed integers expected: {EXPECTED}, but got: {result}')

    def test_divide_negative_integers(self):
        calc = Calculator(-6, -3)
        EXPECTED = 2
        result = calc.divide()
        self.assertEqual(result, EXPECTED,
         f'division between negative integers expected: {EXPECTED}, but got: {result}')

