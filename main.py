from motor_data import *
from motor_list import *
from power_calc_functions import *

if __name__ == "__main__":
    
    md = MotorData(motors4P)
    ml = MotorList(motorList)

    p_other = [50, 1]

    pin = pin_tot_calc(md, ml, p_other)
    qin = qin_tot_calc(md, ml, p_other)
    pf = pf_calc(pin, qin)
    
    print("Starting Pin =", round(pin, 3), "kW")
    print("Starting Qin =", round(qin, 3), "kVA")
    print("------------ cosφ =", round(pf, 3),"------------")
    
    pin, qin = sync_factor_calc(pin, qin, 0.72)
    
    print("Taking to consideration the sync factor, Pin =", round(pin, 3), "kW")
    print("Taking to consideration the sync factor, Qin =", round(qin, 3), "kVA")
    print("------------ cosφ =", round(pf, 3),"------------")
    
    if not pf == 0.95:
        print("cosφ need to be 0.95, calculating compensation")
        q_comp = q_comp_calc(pin, qin)
        print("Q compensation is", round(q_comp, 3), "kVA")
        qin = qin + q_comp
        pf = pf_calc(pin, qin)

    print("Total Pin =", round(pin, 3), "kW")
    print("Total Qin =", round(qin, 3), "kVA")
    print("------------ cosφ =", round(pf, 3),"------------")

    