from flask_app.config.mysqlconnection import MySQLConnection



class Robots:
    def __init__(self,data):
        self.id_robot=data["id_robot"]
        self.name=data["name"]
        self.type=data["type"]
        self.power=data["power"]
# getALLROBOTS
    @classmethod
    def get_all(cls):
        query ="SELECT * FROM robots;"

        results = MySQLConnection("fullstack").query_db(query)

        robots=[]

        for robot in results:
            robots.append(robot)
            
            
        return robots
#get One Robot
    @classmethod
    def oneRobot(cls,data):
        query  = "SELECT * FROM robots WHERE id_robot = %(id_robot)s";
        result = MySQLConnection('fullstack').query_db(query,data)
        return cls(result[0])
#AddRobot Route to the template
    @classmethod
    def AddRobot(cls,data):
        query = "INSERT INTO robots (name,type,power) VALUES (%(name)s,%(type)s,%(power)s);"

        # comes back as the new row id
        result = MySQLConnection('fullstack').query_db(query,data)
        
        return result
    
    
#Update One Robot
    @classmethod
    def fixTheRobot(cls,data):
        query = "UPDATE robots SET name=%(name)s,type=%(type)s,power=%(power)s WHERE id_robot = %(id_robot)s;"
        return MySQLConnection('fullstack').query_db(query,data)
#delete Robot
    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM robots WHERE id_robot = %(id_robot)s;"
        return MySQLConnection('fullstack').query_db(query,data)