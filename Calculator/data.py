import math

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return "Error:{e}"
    
def factorial(value):
    try:
        return math.factorial(value)
    except Exception as e:
        return "Error:{e}"

def square_root(value):
    try:
        return math.sqrt(value)
    except Exception as e:
        return "Error:{e}"

def cos(value):
    try:
        return math.cos(math.radians(value))
    except Exception as e:
        return "Error:{e}"
    
def sin(value):
    try:
        return math.sin(math.radians(value))
    except Exception as e:
        return "Error:{e}"

def tan(value):
    try:
        return math.tan(math.radians(value))
    except Exception as e:
        return "Error:{e}"
    
def pi():
    try:
        return math.pi
    except Exception as e:
        return "Error:{e}"
    
def cosh(value):
    try:
        return math.cosh(value)
    except Exception as e:
        return "Error:{e}"
    
def sinh(value):
    try:
        return math.sinh(value)
    except Exception as e:
        return f"Error: {e}"

def tanh(value):
    try:
        return math.tanh(value)
    except Exception as e:
        return "Error:{e}"
    
def log(value):
    try:
        return math.log2(value)
    except Exception as e:
        return "Error:{e}"

def log10(value):
    try:
        return math.log10(value)
    except Exception as e:
        return "Error:{e}"
    
def power(x, value):
    try:
        result = x ** value
        return result
    except Exception as e:
        return f"Error: {e}"