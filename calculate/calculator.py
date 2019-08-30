from transitions import Machine

class Calculator(object):
	pass

calculator = Calculator()

machine = Machine(model=calculator, states=['initial', 'transition from initial', 'transition', 'transition from transition', 'trailing', 'transition from trailing', 'equal'], initial='initial')