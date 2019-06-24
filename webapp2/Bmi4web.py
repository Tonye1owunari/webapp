from flask import Flask, render_template, request

app = Flask(__name__)
   
@app.route("/")
@app.route("/login")
def login()->"html":
    return render_template("login.html")

@app.route("/name.py", methods=["post"])
def User_name()->"html":
    Username = request.form["username"]
    return render_template("welcome.html", Name=Username)

@app.route("/input")
def input():
    return render_template("input.html")   

@app.route("/bmi.py", methods=["post"])
def User_data(): 
    name = str(request.form["username"])
    Weight = float(request.form["weight"])
    Height = float(request.form["height"])
    bmi = Weight/Height**2
    if bmi > 25:
        return render_template("output.html", Result=round(bmi, 1), Say="", Outcome="%s, you are OVERWEIGHT!"%name, Lets="Let's start you off on some weight loss exercise tips...")
    else:
        return render_template("output.html", Result=round(bmi, 1), Say="That's great!", Outcome="%s, you are NOT OVERWEIGHT!"%name, Lets="Let's help you stay in shape...")

   


if __name__ == '__main__':
    app.run(debug=True)