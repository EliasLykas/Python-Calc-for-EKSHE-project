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

def calc_pf(p, q):

    pf = math.cos(math.atan(q/p))

    return pf

def q_comp_calc(Pin, Qin):
    
    q_comp = 0
    
    qin_tot = Pin * math.tan(math.acos(0.95))

    q_comp = qin_tot - Qin

    return q_comp

def sync_factor_calc(Pin, Qin, sf):

    s_sync = [Pin * sf, Qin * sf]

    return s_sync


if __name__ == "__main__":
    
    md = MotorData(motors4P)
    ml = MotorList(motorList1)

    p_other = [50, 1]

    pin = pin_tot(md, ml, p_other)
    qin = qin_tot(md, ml, p_other)
    pf = calc_pf(pin, qin)

    pin, qin = sync_factor_calc(pin, qin, 0.72)
    
    print("Starting Pin =", round(pin, 3), "kW")
    print("Starting Qin =", round(qin, 3), "kVA")
    print("------------", round(pf, 3),"------------")
    
    if not pf == 0.95:
        print("cosφ need to be 0.95, calculating compensation")
        q_comp = q_comp_calc(pin, qin)
        print("Q compensation is", round(q_comp, 3), "kVA")
        qin = qin + q_comp
        pf = calc_pf(pin, qin)

    print("Total Pin =", round(pin, 3), "kW")
    print("Total Qin =", round(qin, 3), "kVA")
    print("------------", round(pf, 3),"------------")

    