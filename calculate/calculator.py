from transitions import Machine

class Calculator(object):

	def __init__(self):
		self.after_initial()

	def after_initial(self):
		self.number1 = 0
		self.operation1 = '+'
		self.number2 = 0
		self.operation2 = '+'
		self.display = self.number1

	def after_digit(self, event):
		print('after_digit')
		pass

	def after_operation(self, event):
		print('after_digit')
		pass

	def after_equal(self, event):
		print('after_equal')
		pass

states = ['initial', 'transition_from_initial', 'transition', 'transition_from_transition', 'trailing', 'transition_from_trailing', 'equal']

transitions = [
	{ 'trigger': 'reset', 'source': 'initial', 'dest': 'initial', 'after': 'after_initial' },
	{ 'trigger': 'digit', 'source': 'initial', 'dest': 'transition from initial', 'after': 'after_digit' },
	{ 'trigger': 'operation', 'source': 'initial', 'dest': 'transition', 'after': 'after_operation' },
	{ 'trigger': 'equal', 'source': 'initial', 'dest': 'equal', 'after': 'after_equal' },
]

calculator = Calculator()

machine = Machine(model=calculator, states=states, transitions=transitions, initial='initial', send_event=True)