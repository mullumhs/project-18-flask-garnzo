from flask import Flask
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
    if operation == "+":
        num = num1 + num2
        print(num)
    elif operation == "-":
        num = num1 - num2
        print(num)
    elif operation == "*":
        num = num1 * num2
        print(num)
    else:
        num = num1 / num2
        print(num)

    # E.g. if operation = "add" then result = num1 + num2

    return f'{num1} {operation} {num2} = {result}'

if __name__ == '__main__':
    app.run(debug=True)