
from flask import Flask,render_template,request,session,redirect

app = Flask(__name__)


app.secret_key="Omega"


@app.route("/")
def index():

    return render_template("index.html")
##############################
@app.route("/result")
def result():

    return render_template("result.html")
###################################

@app.route("/form", methods=["POST"])
def form():
        session["firstName"]=request.form["first_name"]
        session["LastName"]=request.form["last_name"]
        session["PhoneNumber"]=request.form["phone"]

        return redirect("/result")

















if __name__=='__main__':
    app.run(debug=True)