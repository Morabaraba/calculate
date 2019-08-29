from decimal import Decimal


def ensure_decimal(func): 
    '''Ensure kwargs `number1` and `number2` is always of datatype Decimal'''
    def wrapper(*args, **kwargs): 
        #import pdb; pdb.set_trace()
        kwargs['number1'] = Decimal(kwargs.get("number1"))
        kwargs['number2'] = Decimal(kwargs.get("number2"))        
        return func(*args, **kwargs) 
    return wrapper 


class Calculator:
    @classmethod
    @ensure_decimal
    def addition(cls, number1, number2):
        return number1 + number2
    
    @classmethod
    def subtraction(cls, number1, number2):
        return number1 - number2
    
    @classmethod
    def multiplication(cls, number1, number2):
        return number1 * number2
    
    @classmethod
    def division(cls, number1, number2):
        return number1 / number2