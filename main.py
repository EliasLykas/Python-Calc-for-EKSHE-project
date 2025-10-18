from motor_data import *
from motor_list import *
import math

def pin_tot(motor_data_obj, motor_list_obj, p_extra):
    
    pin = 0
        
    for motor in motor_list_obj.dataset:
        pin = pin + motor_data_obj.calc_pin(motor[0],motor[1])

    pin = pin + p_extra[0]

    return pin    

def qin_tot(motor_data_obj, motor_list_obj, p_extra):
    qin = 0
        
    for motor in motor_list_obj.dataset:
        qin = qin + motor_data_obj.calc_qin(motor[0],motor[1])

    qin = qin + p_extra[0] * math.tan(math.acos(p_extra[1]))

    return qin 

def calc_pf(motor_data_obj, motor_list_obj, p_extra):

    q = qin_tot(motor_data_obj, motor_list_obj, p_extra)
    p = pin_tot(motor_data_obj, motor_list_obj, p_extra)

    pf = math.cos(math.atan(q/p))

    return pf

if __name__ == "__main__":
    
    md = MotorData(motors4P)
    ml = MotorList(motorList1)

    p_other = [50, 1]

    pin = round(pin_tot(md, ml, p_other), 3)
    qin = round(qin_tot(md, ml, p_other), 3)
    pf = round(calc_pf(md, ml, p_other), 3)
    

    print("total Pin =", pin, "kW")
    print("total Qin =", qin, "kVA")
    print("------------", pf,"------------")