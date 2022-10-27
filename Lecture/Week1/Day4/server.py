#server.py 
# we import flask
from flask import Flask , render_template
app = Flask(__name__)






@app.route("/")
def hello_world():
    return " World!"


@app.route("/info")

def hello():
    num = 12
    return render_template("index.html",myData=num)

@app.route("/student/<name>")
def name_of_student(name="give me a name"):
    return f"my name is {name} !!"





















if __name__=="__main__":
    app.run(debug=True)
