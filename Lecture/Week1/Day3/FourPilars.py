class Lamp:
    def __init__(self,color,size,light_color="warm white",is_on=False,brightness=100,is_luble_brok=False):
        self.color = color 
        self.size = size 
        self.light_color = light_color 
        self.is_on = is_on 
        self.brightness = brightness
        self.is_luble_brok = is_luble_brok
    def info(self):
        print("**"*50)
        print(f"color :{self.color}")
        print(f"size :{self.size}")
        print(f"light_color :{self.light_color}")
        print(f"is_on :{self.is_on}")
        print(f"brightness :{self.brightness}")
        print(f"is_luble_brok :{self.is_luble_brok}")
        return self
    def Turn_on(self):
        self.is_on= True
        return self
    def adjust_britness(self,direction,amount = 10):
        
        if direction == "rigth":
            if self.brightness + amount <= 100:
                self.brightness += amount
        elif direction =="left":
            if self.brightness -amount >= 0 :
                self.brightness -= amount
        else:
            print("stop you will broke me broo")
        return self








color =input("What color is you lamp? \n>>>")
size = input("What size is you lamp? \n>>>")
lamp1 = Lamp(color,size)
lamp1.info().adjust_britness("rigth").adjust_britness("rigth").info()


class LavaLamp (Lamp):
    def __init__(self,color,size,light_color="warm white",is_on=False,brightness=100,is_luble_brok=False):
        super().__init__(color,size,light_color="warm white",is_on=False,brightness=100,is_luble_brok=False)
    def adjust_britness(self, direction,amount=5):
        super().adjust_britness(direction,amount)
        return self