from flask import Flask,request, render_template

obj = Flask(__name__)  #__name__ is a special variable holding name of module i.e. __main__ here


@obj.route('/')
def welcome():
    return "Welcome to flask"

@obj.route('/cal', methods = ['GET'])
def math_operator():
    operation = request.json["operation"]
    number1= request.json["number1"]
    number2=request.json["number2"]

    if operation == "add":
        result = number1+ number2
    elif operation == "multipy":
        result = number1 * number2  
    elif operation == "division":
        result = number1 / number2   
    else: 
        result = number1 - number2   
    return result        



if __name__ == '__main__':
    obj.run()