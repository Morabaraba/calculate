from flask import Flask, request, jsonify, render_template
from time import time

from .flask_utils import DecimalEncoder
from .calculator import Calculator


app = Flask(__name__)
app.json_encoder = DecimalEncoder
app.config['VERSION'] = int(time())

@app.route('/')
def index():
    return render_template('qunit.html', version = app.config['VERSION'])

@app.route('/')
def test():
    return render_template('qunit.html', version = app.config['VERSION'])

def get_numbers():
    if request.method == 'POST':
        number1 = request.json.get('number1')
        number2 = request.json.get('number2')
    else:
        number1 = request.args.get("number1")
        number2 = request.args.get("number2")
    return (number1, number2, )


@app.route('/ajax/addition', methods=['GET', 'POST'])
def ajax_addition():
    (number1, number2) = get_numbers()
    return jsonify({'answer': Calculator.addition(number1=number1, number2=number2)})


@app.route('/ajax/subtraction', methods=['GET', 'POST'])
def ajax_subtraction():
    (number1, number2) = get_numbers()
    return jsonify({'answer': Calculator.subtraction(number1=number1, number2=number2)})


@app.route('/ajax/multiplication', methods=['GET', 'POST'])
def ajax_multiplication():
    (number1, number2) = get_numbers()
    return jsonify({'answer': Calculator.multiplication(number1=number1, number2=number2)})


@app.route('/ajax/division', methods=['GET', 'POST'])
def ajax_division():
    (number1, number2) = get_numbers()
    return jsonify({'answer': Calculator.division(number1=number1, number2=number2)})
    

@app.route('/ajax/modulo', methods=['GET', 'POST'])
def ajax_modulo():
    (number1, number2) = get_numbers()
    return jsonify({'answer': Calculator.modulo(number1=number1, number2=number2)})


@app.route('/ajax/sqrt', methods=['GET', 'POST'])
def ajax_sqrt():
    (number1, number2) = get_numbers()
    return jsonify({'answer': Calculator.sqrt(number1=number1, number2=0)})