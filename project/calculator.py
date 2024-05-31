from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)


# Define calculator functions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y


def power(x, y):
    return x ** y


def modulo(x, y):
    return x % y


def log(x, base=math.e):
    if x <= 0:
        return "Error: Logarithm undefined for non-positive values"
    if base == 'e':
        return math.log(x)
    else:
        return math.log(x, base)


def sqrt(x):
    if x < 0:
        return "Error: Square root undefined for negative values"
    return math.sqrt(x)


def sin(x):
    return math.sin(math.radians(x))


def cos(x):
    return math.cos(math.radians(x))


def tan(x):
    return math.tan(math.radians(x))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data['operation']
    x = float(data['x'])
    y = float(data.get('y', 0)) 

    if operation == 'add':
        result = add(x, y)
    elif operation == 'subtract':
        result = subtract(x, y)
    elif operation == 'multiply':
        result = multiply(x, y)
    elif operation == 'divide':
        result = divide(x, y)
    elif operation == 'power':
        result = power(x, y)
    elif operation == 'modulo':
        result = modulo(x, y)
    elif operation == 'log':
        base = float(data.get('base', math.e))
        result = log(x, base)
    elif operation == 'sqrt':
        result = sqrt(x)
    elif operation == 'sin':
        result = sin(x)
    elif operation == 'cos':
        result = cos(x)
    elif operation == 'tan':
        result = tan(x)
    else:
        result = 'Invalid operation'

    return jsonify(result=result)


if __name__ == '__main__':
    app.run(debug=True)
