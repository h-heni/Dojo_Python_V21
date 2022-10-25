# what is OOP 

# Object Oriented Programming

#what is object 

# classes => objects
# definition : bleuPrint
#------contain instruction to buil the object
#------constructor function 


# attributes:
#---- the properties that make usp tha class(object)



# methods:
#defenition : the action that object can take 
#defenition : the function that make up the object

# self
#defenition : self----W to instance of the object

class TheDragon:
    cave = []
    def __init__(self,scale_color,type,size,wing_count,horn_count,likes_gold=True):
        self.scale_color = scale_color
        self.type = type 
        self.size = size
        self.wing_count=wing_count
        self.horn_count = horn_count
        self.likes_gold = likes_gold
        self.is_flying = False
        self.is_eation = False
        TheDragon.cave.append(self)
    def info(self):
        print(f"scale : {self.scale_color}")
        print(f"type: {self.type}")
        print(f"size: {self.size}")
        print(f"wings: {self.wing_count}")
        print(f"horns: {self.horn_count}")
        print(f"eat: {self.is_eation}")
        return self

    # def fly(self):
    #     self.is_flying = True
    # def eat(self):
    #     if self.is_eation:
    #         print("I need To eat")
    #     else:
    #         print("You cannot eat in air")
    #     #classMethods
    #     # def AllDragons(cls):
    #     #     for dargon in cls.cave:
    #     #         dragon.info()




Sunfyre = TheDragon("gold","Rare","BigLarge",6,400)
# print(Sunfyre)

# Sunfyre.fly()

print(Sunfyre.info())

#chaining

# Sunfyre.info().fly().info()
