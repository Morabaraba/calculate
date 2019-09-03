import logging
import unittest

from calculate.calculator import Calculator

#logging.basicConfig(level=logging.DEBUG)
#logging.getLogger('transitions').setLevel(logging.INFO)

log = logging.getLogger("test")

class TestCalculator(unittest.TestCase):
	"""
	Test calculator state machine
	"""

	def test_add(self):
		"""
		Test the addition of two numbers
		"""
		calculator = Calculator()
		log.debug(calculator)
		calculator.number(number=4)
		log.debug(calculator)
		calculator.number(number=2)
		log.debug(calculator)
		calculator.operation(operation='+')
		log.debug(calculator)
		calculator.number(number=3)
		log.debug(calculator)
		calculator.number(number=3)
		log.debug(calculator)
		calculator.number(number=3)
		log.debug(calculator)
		calculator.equal()
		log.debug(calculator)
		self.assertEqual(calculator.display, '375')

	def test_subtraction(self):
		"""
		Test the subtraction of two numbers
		"""
		calculator = Calculator()
		log.debug(calculator)
		calculator.number(number=4)
		log.debug(calculator)
		calculator.number(number=2)
		log.debug(calculator)
		calculator.operation(operation='-')
		log.debug(calculator)
		calculator.number(number=3)
		log.debug(calculator)
		calculator.number(number=3)
		log.debug(calculator)
		calculator.number(number=3)
		log.debug(calculator)
		calculator.equal()
		log.debug(calculator)
		self.assertEqual(calculator.display, '-291')

	def test_multiplication(self):
		"""
		Test the multiplication of two numbers
		"""
		calculator = Calculator()
		calculator.number(number=9)
		log.debug(calculator)
		calculator.operation(operation='*')
		log.debug(calculator)
		calculator.number(number=3)
		log.debug(calculator)
		calculator.equal()
		log.debug(calculator)
		self.assertEqual(calculator.display, '27')

	def test_division(self):
		"""
		Test the division of two numbers
		"""
		calculator = Calculator()
		calculator.number(number=9)
		log.debug(calculator)
		calculator.operation(operation='/')
		log.debug(calculator)
		calculator.number(number=3)
		log.debug(calculator)
		calculator.equal()
		log.debug(calculator)
		self.assertEqual(calculator.display, '3')

	def test_add_equal(self):
		"""
		Test the add with equal
		"""
		calculator = Calculator()
		calculator.number(number=9)
		log.debug(calculator)
		calculator.operation(operation='+')
		log.debug(calculator)
		calculator.number(number=3)
		log.debug(calculator)
		calculator.equal()
		log.debug(calculator)
		self.assertEqual(calculator.display, '12')
		calculator.equal()
		self.assertEqual(calculator.display, '15')
		

	def test_precedence_add_multiply(self):
		'''
		Test precedence by adding and multiplying
		'''
		calculator = Calculator()
		log.debug(calculator)
		calculator.number(number=9)
		log.debug(calculator)
		calculator.operation(operation='+')
		log.debug(calculator)
		calculator.number(number=5)
		log.debug(calculator)
		calculator.operation(operation='*')
		log.debug(calculator)
		calculator.number(number=2)
		log.debug(calculator)
		calculator.equal()
		log.debug(calculator)
		self.assertEqual(calculator.display, '19')

	def test_precedence_add_multiply_subtraction_division(self):
		'''
		Test precedence by adding, multiplying, subtraction, division
		'''
		calculator = Calculator()
		log.debug(calculator)
		calculator.number(number=9)
		log.debug(calculator)
		calculator.operation(operation='+')
		log.debug(calculator)
		calculator.number(number=5)
		log.debug(calculator)
		calculator.operation(operation='*')
		log.debug(calculator)
		calculator.number(number=2)
		log.debug(calculator)
		calculator.operation(operation='-')
		log.debug(calculator)
		calculator.number(number=9)
		log.debug(calculator)
		calculator.operation(operation='/')
		log.debug(calculator)
		calculator.number(number=2)
		log.debug(calculator)
		calculator.equal()
		log.debug(calculator)
		self.assertEqual(calculator.display, '14.5')

	def test_add_equal_multiply_equal(self):
		"""
		Test addition, equal, multiply, equal
		"""
		calculator = Calculator()
		log.debug(calculator)
		calculator.number(number=4)
		log.debug(calculator)
		calculator.number(number=2)
		log.debug(calculator)
		calculator.operation(operation='+')
		log.debug(calculator)
		calculator.number(number=3)
		log.debug(calculator)
		calculator.number(number=3)
		log.debug(calculator)
		calculator.number(number=3)
		log.debug(calculator)
		calculator.equal()
		log.debug(calculator)
		self.assertEqual(calculator.display, '375')
		calculator.number(number=4)
		log.debug(calculator)
		calculator.number(number=2)
		log.debug(calculator)
		calculator.operation(operation='*')
		log.debug(calculator)
		calculator.number(number=3)
		log.debug(calculator)
		calculator.equal()
		self.assertEqual(calculator.display, '126')
		
	def test_number_reset(self):
		"""
		Test number and reset
		"""
		calculator = Calculator()
		log.debug(calculator)
		calculator.number(number=4)
		log.debug(calculator)
		calculator.number(number=2)
		log.debug(calculator)
		calculator.reset()
		self.assertEqual(calculator.display, '0')

	def test_add_equal_multiply_reset_division(self):
		"""
		Test addition, equal, multiply, reset, division
		"""
		calculator = Calculator()
		log.debug(calculator)
		calculator.number(number=4)
		log.debug(calculator)
		calculator.number(number=2)
		log.debug(calculator)
		calculator.operation(operation='+')
		log.debug(calculator)
		calculator.number(number=3)
		log.debug(calculator)
		calculator.number(number=3)
		log.debug(calculator)
		calculator.number(number=3)
		log.debug(calculator)
		calculator.equal()
		log.debug(calculator)
		self.assertEqual(calculator.display, '375')

		calculator.number(number=4)
		log.debug(calculator)
		calculator.number(number=2)
		log.debug(calculator)
		calculator.operation(operation='*')
		log.debug(calculator)
		calculator.reset()
		self.assertEqual(calculator.display, '0')
		
		calculator.number(number=9)
		log.debug(calculator)
		calculator.operation(operation='/')
		log.debug(calculator)
		calculator.number(number=3)
		log.debug(calculator)
		calculator.equal()
		log.debug(calculator)
		self.assertEqual(calculator.display, '3')
		
if __name__ == '__main__':
    unittest.main()