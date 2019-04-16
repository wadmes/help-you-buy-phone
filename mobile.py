import math



#THe value rule should be as followed:
#minimal: the acceptable minimal value
#minimal - zero:  the zero point value 
def log(value,minimal,best = 100,minimal_point = 0.8):
    if(value<minimal):
        return minimal_point*value/minimal
    else:
        return minimal_point+ (1-minimal_point)*(value- minimal)/(best-minimal)
def normalize(value,best,worst):
    coefficient = 100.0/(best - worst)
    b = 100.0*worst/(worst - best)
    #return max(min(value*coefficient + b, 100),0)
    return value*coefficient + b
class Phone:
    def __init__(self,name, price, photo,efficiency,battery,screen,weight,width,material,beauty,charge,screen_unlock,wireless_charge,water_defence):
        self.point = []
        self.name = name
        self.price = price
        self.point.append(log(photo,50,minimal_point= 0.3) * 0.3)
        self.point.append(log(efficiency,50,minimal_point = 0.7) * 1.5)
        self.point.append(log(battery,80) * 1.2)
        self.point.append(log(screen,90,minimal_point= 0.7) * 0.8)
        self.point.append(log(normalize(width,70,77),80) * 0.4)
        self.point.append(log(normalize(weight,150,210),80) * 0.6)
        self.point.append(log(material,80) * 0.4)
        self.point.append(log(beauty,60) * 0.2)
        self.point.append(normalize(charge,40,15)/100* 0.5)
        self.point.append(screen_unlock * 0.2)
        self.point.append(wireless_charge * 0.4)
        self.point.append(water_defence * 0.3)
        #print(self.name)
        #print("photo,efficiency,battery,screen,weight,width,material,beauty,charge,screen_unlock,wireless_charge,water_defence")
        #print([ '%.2f' % elem for elem in self.point ])
        print(self.name,"最终总分为",'%.2f' % sum(self.point),"价格为",price,",综上 性价比为",'%.2f' % ((sum(self.point) - 3.67)/price*10000))

class liweiPhone:
    def __init__(self,name, price, photo,efficiency,battery,screen,weight,width,material,beauty,charge,screen_unlock,wireless_charge,water_defence):
        self.point = []
        self.name = name
        self.price = price
        self.point.append(log(photo,50,minimal_point= 0.3) * 1.2)
        self.point.append(log(efficiency,50,minimal_point = 0.7) * 2.5)
        self.point.append(log(battery,80) * 0.7)
        self.point.append(log(screen,90,minimal_point= 0.7) * 0.6)
        self.point.append(log(normalize(width,70,77),80) * 0.9)
        self.point.append(log(normalize(weight,150,190),80) * 0.5)
        self.point.append(log(material,80) * 0.6)
        self.point.append(log(beauty,60) * 0.7)
        self.point.append(normalize(charge,40,15)/100* 0.7)
        self.point.append(screen_unlock * 0.25)
        self.point.append(wireless_charge * 0.35)
        self.point.append(water_defence * 0.35)
        #print(self.name)
        print("photo,efficiency,battery,screen,weight,width,material,beauty,charge,screen_unlock,wireless_charge,water_defence")
        print([ '%.2f' % elem for elem in self.point ])
        print(self.name,"最终总分为",'%.2f' % sum(self.point),"价格为",price,",综上 性价比为",'%.2f' % ((sum(self.point) - 3.67)/price*1000))
            #name, price, photo,efficiency,battery,screen,width,weight,material,beauty,charge,screen_unlock,wireless_charge,water_defence
print("photo,efficiency,battery,screen,weight,width,material,beauty,charge,screen_unlock,wireless_charge,water_defence")
mi9 = Phone("mi9",3300,85,100,70,70,173,74.7,70,65,27,1,1,0)
s10 = Phone("s10",4100,100,100,70,100,157,70.4,100,80,15,0.7,1,1)
#s10plus = Phone("s10plus",4800,102,100,100,100,175,74.1,100,80,15,0.7,1,1)
mate20 = Phone("mate20",3300,85,90,100,70,188,77.2,100,65,22.5,0,0,0)
mate20pro = Phone("mate20PRO",4260,115,90,100,80,189,72.3,120,45,40,1,1,1)
#mix3 = Phone("mix3",2400,75,70,70,70,218,84.6,90,100,18,0,1,0)
#s9plus = Phone("s9+",3200,85,70,80,90,189,73.8,100,85,15,0,0,1)
s9 = Phone("s9",2700,80,50,65,90,163,68.7,100,85,15,0,1,1)
honorv20 = Phone("honorv20",2700,80,90,100,60,180,75.4,60,70,22.5,0,0,0)
#mix2 = Phone("mix2",1600,50,60,70,55,187,74.6,80,55,18,0,0,0)
honor20 = Phone("honor20",3300,100,90,100,70,165,71.5,65,65,22.5,1,1,0)
meizu16 = Phone("meizu16",2200,80,75,65,70,152,73.2,70,85,22,0.7,0,0)
#i7 = Phone("i7",1500,60,60,70,70,158,70,100,0,5,0,0,0)
#mi6 = Phone("mi6",400,20,60,40,30,182,70.5,70,40,10,0,0,0)
p30 = Phone("p30",3500,115,95,90,70,160,71,100,80,22.5,1,0,0)
p30pro = Phone("p30pro",3900,130,100,110,65,192,73.4,100,80,40,1,1,1)
#p30pro = Phone('p30pro',3800,130,100,100,80,192,73.4,120,65,40,1,1,1)
mi9se = Phone("mi9se",2200,80,55,70,70,155,70.5,70,70,18,1,0,0)
XR = Phone("XR",4500,80,150,100,85,194,75.7,70,40,25,0,1,0.8)
#mi8 = Phone("mi8",1560,75,75,75,60,175,74.8,70,40,18,0,0,0)
a80 = Phone("A80",2800,85,70,120,80,206,76,70,90,25,1,0,0)