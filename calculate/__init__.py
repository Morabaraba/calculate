from flask import Flask, request, jsonify, render_template
from time import time

from .flask_utils import DecimalEncoder
from .calculator import Calculator


app = Flask(__name__)
app.json_encoder = DecimalEncoder
app.config['VERSION'] = int(time())

@app.route('/')
def index():
    return render_template('index.html', version = app.config['VERSION'])
    

@app.route('/ajax/addition')
def ajax_addition():
    number1 = request.args.get("number1")
    number2 = request.args.get("number2")
    return jsonify({'answer': Calculator.addition(number1=number1, number2=number2)})


@app.route('/ajax/subtraction')
def ajax_subtraction():
    number1 = request.args.get("number1")
    number2 = request.args.get("number2")
    return jsonify({'answer': Calculator.subtraction(number1=number1, number2=number2)})


@app.route('/ajax/multiplication')
def ajax_multiplication():
    number1 = request.args.get("number1")
    number2 = request.args.get("number2")
    return jsonify({'answer': Calculator.multiplication(number1=number1, number2=number2)})


@app.route('/ajax/division')
def ajax_division():
    number1 = request.args.get("number1")
    number2 = request.args.get("number2")
    return jsonify({'answer': Calculator.division(number1=number1, number2=number2)})
    

@app.route('/ajax/modulo')
def ajax_modulo():
    number1 = request.args.get("number1")
    number2 = request.args.get("number2")
    return jsonify({'answer': Calculator.modulo(number1=number1, number2=number2)})


@app.route('/ajax/sqrt')
def ajax_sqrt():
    number1 = request.args.get("number1")
    number2 = '1' # fake number
    return jsonify({'answer': Calculator.sqrt(number1=number1, number2=number2)})