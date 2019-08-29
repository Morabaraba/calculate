from flask import Flask, escape, request, jsonify

from .flask_utils import  DecimalEncoder
from .calculator import Calculator


app = Flask(__name__)
app.json_encoder = DecimalEncoder

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
    

@app.route('/ajax/addition')
def addition():
    number1 = request.args.get("number1")
    number2 = request.args.get("number2")
    return jsonify({'answer': Calculator.addition(number1=number1, number2=number2)})
