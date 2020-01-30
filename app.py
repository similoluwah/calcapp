from flask import Flask, request, url_for, render_template, jsonify
from sympy import *
init_printing(pretty_print = True)
app = Flask(__name__)

@app.route("/")
#Declare the main function for the application
def home():
    return render_template("index.html")

@app.route("/basic_calc")

def basic_calc():
    return render_template("basic-calc.html")

@app.route("/derivative-calc")

def derivative_calc():
    return render_template("derivative_calc.html")

@app.route("/symbolic")

def symbolic():
    return render_template("symbolic_math.html")


#Form submission route
@app.route("/send", methods = ['POST'])
def send():
    if request.method == 'POST':
        #Pull data from Input
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        #Performing the Calculations
        if operation == "add":
            sum = float(num1) + float(num2)
            return render_template("basic-calc.html", sum=sum)
        elif operation == "sub":
            sum = float(num1) - float(num2)
            return render_template("basic-calc.html", sum=sum)
        elif operation == "division":
            sum = float(num1) / float(num2)
            return render_template("basic-calc.html", sum=sum)
        elif operation == "multiply":
            sum = float(num1) * float(num2)
            return render_template("basic-calc.html", sum=sum)
        else:
            return render_template("basic-calc.html")
        
@app.route("/send-symbolic", methods = ['POST'])

def sendsymbolic():
    if(request.method == 'POST'):
        #Pull data from the form input
        symbolicfunc = request.form['symbolicfunc']
        operationsymbolic = request.form['operationsymbolic']

        #Performing Calculations
        if operationsymbolic == "simplify":
            result = simplify(symbolicfunc)
            return render_template("symbolic_math.html", result = result)
        
        elif operationsymbolic == "expand":
            result = expand(symbolicfunc)
            return render_template("symbolic_math.html", result = result)

        elif operationsymbolic == "factorize":
            result = factor(symbolicfunc)
            return render_template("symbolic_math.html", result = result)

        
        
        else:
            return render_template("symbolic_math.html")


#derivative calculator
@app.route("/derive", methods = ['POST'])

def derive():
    if(request.method == 'POST'):
        #Pull data from the form inputs 
        operationcalculus = request.form['operationcalculus']
        lowerlimit = request.form['lower-limit']
        upperlimit = request.form['upper-limit']
        function = request.form['func']

        #Performing calculations/evaluations
        if operationcalculus == "diff":
            result = diff(function)
            return render_template("derivative_calc.html",result = result, operationcalculus = operationcalculus)
        
        elif operationcalculus == "int":
            x = Symbol('x')
            result_int= integrate(function)
            result_bound = integrate(function, (x, lowerlimit, upperlimit))
            return render_template("derivative_calc.html", result_int= result_int, result_bound = result_bound, operationcalculus = operationcalculus)

        else: 
            return render_template("derivative_calc.html")

        

if (__name__ == "__main__"):
    app.run(debug = True)