import numpy as np



#This will simulate a ball being thrown in a balistic arc.
#The lanch area and landing area are at the same height becuase that simplifyes the math significantly
#I will add both varried height and varried mass to the calculations later
class ball:
    def __init__(self, g=9.81):
        self.init_height = 0
        self.theta = 0
        self.magnatude = 0
        self.magnatude_x = 0
        self.magantude_y = 0
        self.time_final = 0
        self.g = g
        self.time = 0
        self.values = []
    
    def __repr__(self):
        #this will allow for the printing of values to the console
        return "Theta: " + str(self.theta) + ', Magnatude: ' + str(self.magnatude) + ', Magnatude_x: ' + str(self.magnatude_x) + \
            ' Magnatude_y: ' + str(self.magantude_y) + ' Time Final: ' + str(self.time_final) + ' Gravity: ' + str(self.g)

    def throw(self, theta, magnatude, launch_height=0):
        self.init_height = launch_height
        self.theta = np.radians(theta)
        self.magnatude = magnatude
        self.magnatude_x = np.cos(self.theta) * self.magnatude
        self.magnatude_y = np.sin(self.theta) * self.magnatude
        if self.init_height == 0:
            self.time_final = (self.magnatude_y * 2)/self.g
        if self.init_height != 0:
            while True:
                self.time_final = self.time_final + 0.01
                y = self.init_height + self.magnatude_y*self.time_final - (1/2)*self.g*(self.time_final**2)
                if y <= 0:
                    break
        self.time = np.linspace(0, self.time_final, 100)
        for i in range(len(self.time)):
            self.values.append((self.magnatude_x*(self.time[i]), \
                                self.init_height + self.magnatude_y*(self.time[i])-(1/2)*self.g*((self.time[i])**2)))
            
        return self.values
    
    def clear_list(self):
        self.labels = []
        self.data = []
        self.values = []
    
    def reset(self):
        self.theta = 0
        self.magnatude = 0
        self.magnatude_x = 0
        self.magantude_y = 0
        self.time_final = 0
        self.time = 0
        self.values = []