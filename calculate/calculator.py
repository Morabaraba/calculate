from decimal import Decimal

from transitions import Machine

class Calculator(object):

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
		{ 'trigger': 'operation', 'source': 'initial', 'dest': 'transition', 'after': 'after_operation1' },
		{ 'trigger': 'equal', 'source': 'initial', 'dest': 'equal', 'after': 'after_equal' },

		# state 2: transition_from_initial
		{ 'trigger': 'reset', 'source': 'transition_from_initial', 'dest': 'transition_from_initial', 'conditions': 'is_number1_not_zero', 'after': 'after_initial' },
		{ 'trigger': 'reset', 'source': 'transition_from_initial', 'dest': 'initial', 'conditions': 'is_number1_not_zero', 'after': 'after_initial' },
		{ 'trigger': 'number', 'source': 'transition_from_initial', 'dest': 'transition_from_initial', 'after': 'after_number1' },
		{ 'trigger': 'operation', 'source': 'transition_from_initial', 'dest': 'transition', 'after': 'after_operation1' },
		{ 'trigger': 'equal', 'source': 'transition_from_initial', 'dest': 'equal', 'after': 'after_equal' },

		# state 3: transition
		{ 'trigger': 'reset', 'source': 'transition', 'dest': 'transition_from_initial', 'after': 'after_reset1' },
		{ 'trigger': 'number', 'source': 'transition', 'dest': 'transition_from_transition', 'after': 'after_number2' },
		{ 'trigger': 'operation', 'source': 'transition', 'dest': 'transition', 'after': 'after_operation1' },
		{ 'trigger': 'equal', 'source': 'transition', 'dest': 'equal', 'after': 'after_equal' },
	
		# state 4: transition_from_transition
		{ 'trigger': 'equal', 'source': 'transition_from_transition', 'dest': 'equal', 'after': 'after_equal' },
		{ 'trigger': 'reset', 'source': 'transition_from_transition', 'dest': 'transition_from_transition', 'conditions': 'is_number2_not_zero', 'after': 'after_reset2' },
		{ 'trigger': 'reset', 'source': 'transition_from_transition', 'dest': 'initial', 'conditions': 'is_number2_zero', 'after': 'after_initial' },
		{ 'trigger': 'number', 'source': 'transition_from_transition', 'dest': 'transition_from_transition', 'after': 'after_number2' },
		{ 'trigger': 'operation', 'source': 'transition_from_transition', 'dest': 'transition', 'conditions': 'is_operation_simple', 'after': 'after_operation2' },
		{ 'trigger': 'operation', 'source': 'transition_from_transition', 'dest': 'transition', 'conditions': 'is_operation_complex', 'after': 'after_operation2' },
		{ 'trigger': 'operation', 'source': 'transition_from_transition', 'dest': 'trailing', 'conditions': 'is_operation_trailing', 'after': 'after_operation_trailing' },

		# state 5: trailing
		{ 'trigger': 'equal', 'source': 'trailing', 'dest': 'equal', 'after': 'after_trailing_equal' },
		{ 'trigger': 'reset', 'source': 'trailing', 'dest': 'transition_from_trailing', 'after': 'after_reset_trailing' },
		{ 'trigger': 'number', 'source': 'trailing', 'dest': 'transition_from_trailing', 'after': 'after_number_trailing' },
		{ 'trigger': 'operation', 'source': 'trailing', 'dest': 'trailing', 'conditions': 'is_operation_complex', 'after': 'after_operation2' },
		{ 'trigger': 'operation', 'source': 'trailing', 'dest': 'transition', 'conditions': 'is_operation_simple', 'after': 'after_operation_trailing_simple' },

		# state 6: transition_from_trailing
		{ 'trigger': 'reset', 'source': 'transition_from_trailing', 'dest': 'initial', 'conditions': 'is_number_trailing_zero', 'after': 'after_initial' },
		{ 'trigger': 'reset', 'source': 'transition_from_trailing', 'dest': 'transition_from_trailing', 'conditions': 'is_number_trailing_not_zero', 'after': 'after_reset_trailing' },
		{ 'trigger': 'number', 'source': 'transition_from_trailing', 'dest': 'transition_from_trailing', 'after': 'after_number_trailing' },
		{ 'trigger': 'equal', 'source': 'transition_from_trailing', 'dest': 'equal', 'after': 'after_trailing_equal' },
		{ 'trigger': 'operation', 'source': 'transition_from_trailing', 'dest': 'transition', 'conditions': 'is_operation_simple', 'after': 'after_operation_trailing_simple' },
		{ 'trigger': 'operation', 'source': 'transition_from_trailing', 'dest': 'trailing', 'conditions': 'is_operation_complex', 'after': 'after_operation2' },

		# state 7: equal
		{ 'trigger': 'reset', 'source': 'equal', 'dest': 'transition_from_initial', 'after': 'after_reset1' },
		{ 'trigger': 'number', 'source': 'equal', 'dest': 'transition_from_initial', 'after': 'after_number1' },
		{ 'trigger': 'operation', 'source': 'equal', 'dest': 'transition', 'after': 'after_operation1' },
		{ 'trigger': 'equal', 'source': 'equal', 'dest': 'equal', 'after': 'after_equal' },
	]


	def __init__(self, initial = 'initial'):
		self.machine = Machine(model=self, states=Calculator.states, transitions=Calculator.transitions, initial=initial, send_event=True)
		self.after_initial(event=None)

	def __str__(self):
		return f'{super().__str__()} = <number1 = {self.number1}; operation1 = {self.operation1}; number2 = {self.number2}; operation2 = {self.operation2}; number_trailing = {self.number_trailing}; display = {self.display}; state = {self.state}>'

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
		self.number1 = self.number1 + f'{event.kwargs["number"]}' if self.number1 != '0' else f'{event.kwargs["number"]}' # merge two integers - https://stackoverflow.com/a/50700078
		self.display = self.number1

	def after_number2(self, event):
		self.number2 = self.number2 + f'{event.kwargs["number"]}' if self.number2 != '0' else f'{event.kwargs["number"]}'
		self.display = self.number2

	def after_operation1(self, event):
		self.operation1 = event.kwargs['operation']
		self.display = self.number1

	def after_operation2(self, event):
		self.operation1 = event.kwargs['operation']
		self.number1 = self.perform_operation()
		self.display = self.number1

	def after_operation_trailing(self, event):
		self.operation2 = event.kwargs['operation']
		self.trailing = self.number2

	def after_equal(self, event):
		self.number1 = self.perform_operation()
		self.display = self.number1

	def after_number_trailing(self, event):
		self.number_trailing = self.number_trailing + f'{event.kwargs["number"]}' if self.number_trailing != '0' else f'{event.kwargs["number"]}'
		self.display = self.number_trailing

	def after_trailing_equal(self, event):
		self.number2 = self.perform_operation(number1 = self.number2, operation = self.operation2, number2 = self.number_trailing)
		self.number1 = self.perform_operation()
		self.display = self.number1

	def after_operation_trailing_simple(self, event):
		self.after_trailing_equal()
		self.operation1 = event.kwargs['operation']

	def after_reset_trailing(self, event):
		self.number_trailing = '0'


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
		return self.number2 == '0' and self.operation1 in Calculator.complex_operations

	def is_operation_trailing(self, event):
		return self.operation1 in Calculator.simple_operations

	def is_number_trailing_not_zero(self, event):
		return self.number_trailing != '0'

	def is_number_trailing_zero(self, event):
		return self.number_trailing == '0'


	# ...
	def perform_operation(self, number1 = None, operation = None, number2 = None):
		if not number1:
			number1 = self.number1
		if not operation:
			operation = self.operation1
		if not number2:
			number2 = self.number2

		if operation == '+':
			number = Decimal(number1) + Decimal(number2)
		elif operation == '-':
			number = Decimal(number1) - Decimal(number2)
		elif operation == '*':
			number = Decimal(number1) * Decimal(number2)
		elif operation == '/':
			number = Decimal(number1) / Decimal(number2)
		else:
			raise Exception(f'operation "{operation}" not valid')
		return f'{number}'





