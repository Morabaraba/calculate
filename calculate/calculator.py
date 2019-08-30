from decimal import Decimal

from transitions import Machine



input_numbers = '0123456789.'
input_operations = '+-*/'
input_equal = '='

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
	{ 'trigger': 'reset', 'source': 'transition', 'dest': 'transition_from_initial', 'after': 'after_reset' },
	{ 'trigger': 'number', 'source': 'transition', 'dest': 'transition_from_transition', 'after': 'after_number2' },
	{ 'trigger': 'operation', 'source': 'transition', 'dest': 'transition', 'after': 'after_operation' },
	{ 'trigger': 'equal', 'source': 'transition', 'dest': 'equal', 'after': 'after_equal' },
]



class Calculator(object):

	def __init__(self):
		self.after_initial()


	# after transitions
	def after_initial(self, event):
		self.number1 = '0'
		self.operation1 = '+'
		self.number2 = '0'
		self.operation2 = '+'
		self.number_trailing = '0'
		self.display = self.number1

	def after_reset(self, event):
		self.number1 = '0'

	def after_number1(self, event):
		self.number1 = '0' + event.number
		self.display = self.number1

	def after_number2(self, event):
		self.number2 =  event.number

	def after_operation(self, event):
		self.operation1 = event.operation
		self.number2 = self.number1
		self.display = self.number1

	def after_equal(self, event):
		self.perform_operation()


	# transition conditions
	def is_number1_not_zero(self, event):
		return self.number1 != '0'

	def is_number1_zero(self, event):
		return self.number1 == '0'

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