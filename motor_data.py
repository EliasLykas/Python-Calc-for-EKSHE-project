# This file contains the usefull data about 4-Pole motors form Dr.Dokopoulos book "Oikiakes egkatastasis katanaloton", page.615
# The form of this data is a list (motor) of lists 
# (motors data = [motors horse power (HP), motors output power (kW), motor efficiency (%), motors power factor (pf), Nominal Operating Current (A), Starting Current Multiplyer (Is/In)])
# It also contains usefull funtions to work with this data


import math

motors4P = [
    [0.083, 0.06, 58, 0.74, 0.22, 2.8],
    [0.125, 0.09, 59, 0.74, 0.31, 3.3],
    [0.167, 0.12, 56, 0.75, 0.44, 3.0],
    [0.25,  0.18, 60, 0.75, 0.61, 3.2],
    [0.33,  0.25, 62, 0.78, 0.79, 3.2],
    [0.5,   0.37, 66, 0.76, 1.12, 3.7],
    [0.75,  0.55, 71, 0.80, 1.47, 4.7],
    [1.0,   0.75, 74, 0.80, 1.95, 5.0],
    [1.5,   1.10, 75, 0.81, 2.80, 5.0],
    [2.0,   1.50, 75, 0.82, 3.70, 4.9],
    [3.0,   2.20, 79, 0.82, 5.20, 6.0],
    [4.0,   3.00, 81, 0.81, 6.80, 6.2],
    [5.5,   4.00, 83, 0.80, 9.20, 7.0],
    [7.5,   5.50, 84, 0.85, 11.70, 7.0],
    [10.0,  7.50, 86, 0.85, 15.60, 7.7],
    [15.0, 11.00, 88, 0.84, 22.50, 7.6],
    [20.0, 15.00, 89, 0.85, 30.00, 7.7],
    [25.0, 18.50, 90.5, 0.84, 37.00, 6.2],
    [30.0, 22.00, 91.2, 0.85, 43.00, 6.4],
    [40.0, 30.00, 91.8, 0.86, 58.00, 6.4],
    [50.0, 37.00, 92.3, 0.86, 71.00, 6.7],
    [60.0, 45.00, 93.0, 0.87, 85.00, 6.7],
    [75.0, 55.00, 93.5, 0.87, 102.00, 6.7],
    [100.0, 75.00, 94.3, 0.86, 140.00, 6.7],
    [125.0, 90.00, 94.6, 0.86, 168.00, 6.8],
    [150.0, 110.00, 94.7, 0.86, 205.00, 6.7],
    [180.0, 132.00, 95.1, 0.87, 240.00, 6.9],
    [220.0, 160.00, 95.5, 0.87, 295.00, 7.0],
    [270.0, 200.00, 95.8, 0.87, 365.00, 7.0],
    [340.0, 250.00, 96.0, 0.88, 450.00, 7.0],
    [428.0, 315.00, 96.3, 0.88, 560.00, 7.0],
    [483.0, 355.00, 96.3, 0.88, 640.00, 7.0],
    [544.0, 400.00, 96.5, 0.88, 720.00, 7.0],
]

class MotorData:
    def __init__(self, dataset):
        self.dataset = dataset  

# This function returns the motors list given the motors HP 

    def find_motor(self, hp):
        
        closest = min(self.dataset, key=lambda x: abs(x[0] - hp))
        return closest

#This Function calculates and returns the active power input (Pin) of the motor or motors given its/theirs HP and quantity [HP, quantity]
  
    def calc_pin(self, hp, quantity=1):
        
        motor = self.find_motor(hp)
        HP, kW, eff, pf, In, Ist = motor

        pin = kW / (eff / 100)
        pin_tot = pin * quantity

        return pin_tot

#This Function calculates and returns the apparent power input (Qin) of the motor or motors given its/theirs HP and quantity [HP, quantity]

    def calc_qin(self, hp, quantity=1):
        
        motor = self.find_motor(hp)
        HP, kW, eff, pf, In, Ist = motor

        pin = self.calc_pin(hp, 1)

        qin_single = pin * math.tan(math.acos(pf))
        # qin_single = kW * math.tan(math.acos(pf))

        qin_tot = qin_single * quantity

        return qin_tot