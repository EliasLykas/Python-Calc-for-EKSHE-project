"""Small driver script to calculate installed motor power and compensation.

This script composes the motor dataset (`MotorData`), the installation motor
list (`MotorList`) and a set of power calculation utilities. It prints the
installed active power (Pin), apparent power (Qin), applies a synchronizing
factor, checks/prints compensation requirements and demonstrates scaling.

The script intentionally uses the existing simple classes from the project
that expose a `.dataset` attribute and calculation methods such as
`calc_pin` / `calc_qin`.
"""

from motor_data import *
from motor_list import *
from power_calc_functions import *

if __name__ == "__main__":
    
    # Create helper objects from the provided datasets. `MotorData` exposes
    # methods to calculate active/apparent power for a given motor HP.
    md = MotorData(motors4P)

    # `MotorList` simply wraps the list of installed motors (HP, quantity).
    ml = MotorList(motorList)

    # p_other is an extra load on the installation: [P_kW, power_factor]
    p_other = [50, 1]

    # calculating installed power (active and apparent)
    pin = pin_inst = pin_tot_calc(md, ml, p_other)
    qin = qin_inst = qin_tot_calc(md, ml, p_other)

    # overall power factor for the current installation
    pf = pf_calc(pin, qin)

    print("\nInstalled Pin =", round(pin_inst, 3), "kW")
    print("Installed Qin =", round(qin_inst, 3), "kVA")
    print("------------ cosφ =", round(pf, 3),"------------\n")
    
    # applying a synchronizing factor (sf) to represent diversity/usage
    # Example: sf = 0.72 means 72% of installed power is expected to run
    pin, qin = sync_factor_calc(pin_inst, qin_inst, 0.72)
    
    print("Taking to consideration the sync factor, Pin =", round(pin, 3), "kW")
    print("Taking to consideration the sync factor, Qin =", round(qin, 3), "kVA")
    print("------------ cosφ =", round(pf, 3),"------------\n")
    
    pf_avg = pf_check(pf)

    # demonstrate the existing scale_factor_calc utility. Note: the
    # project's `scale_factor_calc` expects the base power and a factor.
    pin = scale_factor_calc(pin, 0.1)

    print("Taking to consideration a scale factor of 0.1, P_futere =", round(pin, 3), "kW\n")
    print("NOTE:The future power factor of the installation depends on the nature of the future load,\na new compensation might be needed to achieve cosφ = 0.95.\n")


    s_contraced = s_contraced_calc(pin, pf_avg)

    print("The total contracted power for the future installation should be =", round(s_contraced[0],3), "<", round(s_contraced[1],3),"kVA\n")

    # checking power factor, calculating required reactive compensation (if any)
    # q_comp = comp_calc(pin, qin, pf)

    # update total apparent power after compensation (if q_comp != 0)
    # qin = qin + q_comp
    # pf_comp = pf_calc(pin, qin)

    # If compensation was applied, print the new totals and corrected pf
    # if not q_comp == 0:
    #     print("Total Pin =", round(pin, 3), "kW")
    #     print("Total Qin =", round(qin, 3), "kVA")
    #     print("------------ cosφ =", round(pf_comp, 3),"------------\n")