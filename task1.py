from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/hello')
def index():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

@app.route('/calc/<int:num1>/<string:operation>/<int:num2>')
def calculator(num1, operation, num2):
    # Program the logic of a calculator here
    if operation == "add":
        num = num1 + num2
        return f'{num1} {operation} {num2} = {num}'
    elif operation == "minus":
        num = num1 - num2
        return f'{num1} {operation} {num2} = {num}'
    elif operation == "times":
        num = num1 * num2
        return f'{num1} {operation} {num2} = {num}'
    elif operation == "devided":
        num = num1 / num2
        return f'{num1} {operation} {num2} = {num}'
    else:
        return("Error")
    # E.g. if operation = "add" then result = num1 + num2

    return num

@app.route('/search')

def search():

    query = request.args.get('q', '')

    category = request.args.get('category', 'all')

    return f'Searching for "{query}" in category: {category}'

if __name__ == '__main__':
    app.run(debug=True)