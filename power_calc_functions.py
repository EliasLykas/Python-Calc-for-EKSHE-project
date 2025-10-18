import math

def pin_tot_calc(motor_data_obj, motor_list_obj, p_extra):
    
    pin = 0
        
    for motor in motor_list_obj.dataset:
        pin = pin + motor_data_obj.calc_pin(motor[0],motor[1])

    pin = pin + p_extra[0]

    return pin    

def qin_tot_calc(motor_data_obj, motor_list_obj, p_extra):
    qin = 0
        
    for motor in motor_list_obj.dataset:
        qin = qin + motor_data_obj.calc_qin(motor[0],motor[1])

    qin = qin + p_extra[0] * math.tan(math.acos(p_extra[1]))

    return qin 

def pf_calc(p, q):

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

