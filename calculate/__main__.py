import click
from transitions.extensions import GraphMachine

from .calculator import Calculator

@click.command()
@click.option('--debug', is_flag=True, help='Enter the python debug repl. (default)')
@click.option('--graph', is_flag=True, help='Draw the calculator state machine.')
@click.option('--output', default='state_diagram.png', help='Used with --graph to specify filename for drawing. (state_diagram.png)')
def main(debug, graph, output):
	calculator = Calculator()
	if graph:
		machine = GraphMachine(model=calculator,  states=Calculator.states, transitions=Calculator.transitions, use_pygraphviz=False)
		machine.get_graph().draw(output, prog='dot')
	else: # default debug
		import pdb; pdb.set_trace()
	
if __name__ == '__main__':
	main()