from decimal import Decimal

from transitions import Machine



input_numbers = '0123456789.'
input_operations = '+-*/'
input_equal = '='

complex_operations = '*/'
simple_operations = '+-'

states = ['initial', 'transition_from_initial', 'transition', 'transition_from_transition', 'trailing', 'transition_from_trailing', 'equal']

transitions = [
	# state 1: initial
	{ 'trigger': 'reset', 'source': 'initial', 'dest': 'initial', 'after': 'after_initial' },
	{ 'trigger': 'number', 'source': 'initial', 'dest': 'transition_from_initial', 'after': 'after_number1' },
	{ 'trigger': 'operation', 'source': 'initial', 'dest': 'transition', 'after': 'after_operation' },
	{ 'trigger': 'equal', 'source': 'initial', 'dest': 'equal', 'after': 'after_equal' },

	# state 2: transition_from_initial
	{ 'trigger': 'reset', 'source': 'transition_from_initial', 'dest': 'transition_from_initial', 'conditions': 'is_number1_not_zero', 'after': 'after_initial' },
	{ 'trigger': 'reset', 'source': 'transition_from_initial', 'dest': 'initial', 'conditions': 'is_number1_not_zero', 'after': 'after_initial' },
	{ 'trigger': 'number', 'source': 'transition_from_initial', 'dest': 'transition_from_initial', 'after': 'after_number1' },
	{ 'trigger': 'operation', 'source': 'transition_from_initial', 'dest': 'transition', 'after': 'after_operation' },
	{ 'trigger': 'equal', 'source': 'transition_from_initial', 'dest': 'equal', 'after': 'after_equal' },

	# state 3: transition
	{ 'trigger': 'reset', 'source': 'transition', 'dest': 'transition_from_initial', 'after': 'after_reset1' },
	{ 'trigger': 'number', 'source': 'transition', 'dest': 'transition_from_transition', 'after': 'after_number2' },
	{ 'trigger': 'operation', 'source': 'transition', 'dest': 'transition', 'after': 'after_operation' },
	{ 'trigger': 'equal', 'source': 'transition', 'dest': 'equal', 'after': 'after_equal' },

	# state 4: transition_from_transition
	{ 'trigger': 'reset', 'source': 'transition_from_transition', 'dest': 'transition_from_transition', 'conditions': 'is_number2_not_zero', 'after': 'after_reset2' },
	{ 'trigger': 'reset', 'source': 'transition_from_transition', 'dest': 'initial', 'conditions': 'is_number2_zero', 'after': 'after_initial' },
	{ 'trigger': 'number', 'source': 'transition_from_transition', 'dest': 'transition_from_transition', 'after': 'after_number2' },
	{ 'trigger': 'operation', 'source': 'transition_from_transition', 'dest': 'transition', 'conditions': 'is_operation_simple', 'after': 'after_operation2' },
	{ 'trigger': 'operation', 'source': 'transition_from_transition', 'dest': 'transition', 'conditions': 'is_operation_complex', 'after': 'after_operation2' },
	{ 'trigger': 'operation', 'source': 'transition_from_transition', 'dest': 'trailing', 'conditions': 'is_operation_trailing', 'after': 'after_operation_trailing' },
	{ 'trigger': 'equal', 'source': 'transition_from_transition', 'dest': 'equal', 'after': 'after_equal' },
	
	# state 5: trailing
	{ 'trigger': 'reset', 'source': 'trailing', 'dest': 'transition_from_trailing', 'conditions': 'is_number1_not_zero', 'after': 'after_initial' },
	{ 'trigger': 'reset', 'source': 'trailing', 'dest': 'initial', 'conditions': 'is_number1_not_zero', 'after': 'after_initial' },
	{ 'trigger': 'number', 'source': 'trailing', 'dest': 'transition_from_initial', 'after': 'after_number1' },
	{ 'trigger': 'operation', 'source': 'trailing', 'dest': 'trailing', 'conditions': 'is_operation_complex', 'after': 'after_operation' },
	{ 'trigger': 'operation', 'source': 'trailing', 'dest': 'transition', 'conditions': 'is_operation_complex', 'after': 'after_operation' },
	{ 'trigger': 'equal', 'source': 'trailing', 'dest': 'equal', 'after': 'after_equal' },

]



class Calculator(object):

	def __init__(self):
		self.after_initial(event=None)


	# after transitions
	def after_initial(self, event):
		self.number1 = '0'
		self.operation1 = '+'
		self.number2 = '0'
		self.operation2 = '+'
		self.number_trailing = '0'
		self.display = self.number1

	def after_reset1(self, event):
		self.number1 = '0'

	def after_reset2(self, event):
		self.number2 = '0'

	def after_number1(self, event):
		self.number1 = self.number1 + event.kwargs['number'] if self.number1 != '0' else event.kwargs['number']
		self.display = self.number1

	def after_number2(self, event):
		self.number2 = self.number2 + event.kwargs['number'] if self.number2 != '0' else event.kwargs['number']
		self.display = self.number2

	def after_operation1(self, event):
		self.operation1 = event.kwargs['operation']
		self.number2 = self.number1
		self.display = self.number1

	def after_operation2(self, event):
		self.operation1 = event.kwargs['operation']
		self.perform_operation()
		self.display = self.number1

	def after_operation_trailing(self, event):
		self.operation2 = event.kwargs['operation']
		self.trailing = self.number2

	def after_equal(self, event):
		self.perform_operation()


	# transition conditions
	def is_number1_not_zero(self, event):
		return self.number1 != '0'

	def is_number1_zero(self, event):
		return self.number1 == '0'

	def is_number2_not_zero(self, event):
		return self.number2 != '0'

	def is_number2_zero(self, event):
		return self.number2 == '0'

	def is_operation_simple(self, event):
		return self.number2 == '0'

	def is_operation_complex(self, event):
		return self.number2 == '0' and self.operation1 in complex_operations

	def is_operation_trailing(self, event):
		return self.operation1 in simple_operations


	# ...
	def perform_operation(self):
		if self.operation1 == '+':
			number = Decimal(self.number1) + Decimal(self.number2)
		elif self.operation1 == '-':
			number = Decimal(self.number1) - Decimal(self.number2)
		elif self.operation1 == '*':
			number = Decimal(self.number1) * Decimal(self.number2)
		elif self.operation1 == '/':
			number = Decimal(self.number1) / Decimal(self.number2)
		else:
			raise Exception('operation1 not valid')
		self.number1 = f'{number}'



calculator = Calculator()

machine = Machine(model=calculator, states=states, transitions=transitions, initial='initial', send_event=True)