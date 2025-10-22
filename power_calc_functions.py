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

def comp_calc(Pin, Qin, pf):
    
    q_comp = 0

    if pf_check(pf):

        print("No compensation needed.\n")

        return q_comp

    else:  
        print("calculating compensation....")

        qin_tot = Pin * math.tan(math.acos(0.95))

        q_comp = qin_tot - Qin

        print("Q compensation is", round(q_comp, 3), "kVA\n")

        return q_comp

def sync_factor_calc(Pin, Qin, sf):

    s_sync = [Pin * sf, Qin * sf]

    return s_sync

def pf_check(pf):

    if not pf == 0.95:
        avg_pf = (pf + 0.95) / 2
        print("cosφ need's to be 0.95")
        print("so, average cosφ for the installation is", round(avg_pf, 3), "\n")
        return False
    else:
        return True

def scale_factor_calc(pin, scale ):

    scaled_value = pin * (scale + 1)

    return scaled_value