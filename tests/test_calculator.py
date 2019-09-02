import unittest

from calculate.calculator import Calculator

 
class TestCalculator(unittest.TestCase):
	"""
	Test calculator state machine
	"""
 
	def test_add(self):
		"""
		Test that the addition of two numbers
		"""
		calculator = Calculator()
		#print(calculator)
		calculator.number(number=4)
		#print(calculator)
		calculator.number(number=2)
		#print(calculator)
		calculator.operation(operation='+')
		#print(calculator)
		calculator.number(number=3)
		#print(calculator)
		calculator.number(number=3)
		#print(calculator)
		calculator.number(number=3)
		#print(calculator)
		calculator.equal()
		#print(calculator)
		self.assertEqual(calculator.display, '375')

	def test_subtraction(self):
		"""
		Test that the subtraction of two numbers
		"""
		calculator = Calculator()
		#print(calculator)
		calculator.number(number=4)
		#print(calculator)
		calculator.number(number=2)
		#print(calculator)
		calculator.operation(operation='-')
		#print(calculator)
		calculator.number(number=3)
		#print(calculator)
		calculator.number(number=3)
		#print(calculator)
		calculator.number(number=3)
		#print(calculator)
		calculator.equal()
		#print(calculator)
		self.assertEqual(calculator.display, '-291')

if __name__ == '__main__':
    unittest.main()