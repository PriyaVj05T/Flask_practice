from flask import Flask,request, render_template, jsonify

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
        result = int(number1) + int(number2)
    elif operation == "multipy":
        result =  int(number1) * int(number2)
    elif operation == "division":
        result =  int(number1) / int(number2)  
    else: 
        result =  int(number1) - int(number2) 
    return jsonify(result)        



if __name__ == '__main__':
    obj.run()