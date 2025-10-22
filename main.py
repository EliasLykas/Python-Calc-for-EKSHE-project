from motor_data import *
from motor_list import *
from power_calc_functions import *

if __name__ == "__main__":
    
    md = MotorData(motors4P)
    ml = MotorList(motorList)

    p_other = [50, 1]

    # calculating installed power
    pin = pin_inst = pin_tot_calc(md, ml, p_other)
    qin = qin_inst = qin_tot_calc(md, ml, p_other)
    pf = pf_calc(pin, qin)

    print("\nInstalled Pin =", round(pin_inst, 3), "kW")
    print("Installed Qin =", round(qin_inst, 3), "kVA")
    print("------------ cosφ =", round(pf, 3),"------------\n")
    
    # installing sync factor of 0.72
    pin, qin = sync_factor_calc(pin_inst, qin_inst, 0.72)
    
    print("Taking to consideration the sync factor, Pin =", round(pin, 3), "kW")
    print("Taking to consideration the sync factor, Qin =", round(qin, 3), "kVA")
    print("------------ cosφ =", round(pf, 3),"------------\n")

    # checking power factor, calculating average powerfactor and calculating compensation if needed
    q_comp = comp_calc(pin, qin, pf)
    qin = qin + q_comp
    pf_comp = pf_calc(pin, qin)

    if not q_comp == 0:
        print("Total Pin =", round(pin, 3), "kW")
        print("Total Qin =", round(qin, 3), "kVA")
        print("------------ cosφ =", round(pf_comp, 3),"------------\n")

    pin = scale_factor_calc(pin, 0.1)

    print("Taking to consideration a scale factor of 0.1, P_futere =", round(pin, 3), "kW")
    print("The future power factor of the installation depends on the nature of the future load, and a new compensation might be needed to achieve cosφ = 0.95.\n")