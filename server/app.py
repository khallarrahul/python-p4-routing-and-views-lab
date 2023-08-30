#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(f"{parameter}")
    return f"{parameter}"


@app.route("/count/<int:parameter>")
def count(parameter):
    c = ""
    for num in range(0, parameter):
        print(f"{num}")
        c = c + str(num) + "\n"
    return c


@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    results = 0
    if operation == "div":
        results = num1 / num2
    elif operation == "+":
        results = num1 + num2
    elif operation == "-":
        results = num1 - num2
    elif operation == "*":
        results = num1 * num2
    else:
        results = num1 % num2
    return str(results)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
