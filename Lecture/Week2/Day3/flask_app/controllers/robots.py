from flask import render_template,redirect,request
from flask_app import app
from flask_app.modules.robot import Robots




# getALLROBOTS
@app.route("/")
def index():
    r=Robots.get_all()
    print(r)
    return render_template("index.html",robots=r)

#get One Robot
@app.route('/oneRobot/<int:id>')
def oneRobot(id):
    data ={ 
        "id_robot":id
    }
    return render_template("one_robot.html",robot=Robots.oneRobot(data))

#AddRobot Route to the template
@app.route("/newRobot")
def Form():
    return render_template("new_robot.html")

#AddRobot to my Table 
@app.route('/newRobot',methods=['POST'])
def newR():
    Robots.AddRobot(request.form)
    
    return redirect("/")




#Update One Robot
@app.route('/fixRobot/<int:id>')
def fixRob(id):
    data ={ 
        "id_robot":id
    }
    return render_template("fixRobot.html",robot=Robots.oneRobot(data))

# Update route when he finnish the Update
@app.route('/fixRobot/hi',methods=['POST'])
def update():
    Robots.fixTheRobot(request.form)
    return redirect('/')

#delete Robot
@app.route('/ByBydestroy/<int:id>')
def destroy(id):
    data ={
        'id_robot': id
}
    Robots.destroy(data)
    return redirect('/')