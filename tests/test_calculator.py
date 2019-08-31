from calculate.calculator import Calculator
import unittest
 
class TestAdd(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()