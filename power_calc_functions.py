"""Utilities for calculating installed Pin, Qin and power-factor actions.

The functions in this module operate on the simple objects used by the
project: `motor_data` helper (which must implement `calc_pin`/`calc_qin`) and
a `MotorList`-like object exposing `.dataset` as an iterable of `[hp, qty]`.
"""

import math


def pin_tot_calc(motor_data_obj, motor_list_obj, p_extra):
    """Calculate total active power (Pin) for an installation.

    motor_data_obj: object with method `calc_pin(hp, qty)`
    motor_list_obj: object with attribute `dataset` iterable of [hp, qty]
    p_extra: list-like [P_extra_kW, pf_extra]
    """
    pin = 0

    # Sum Pin contribution from each installed motor
    for motor in motor_list_obj.dataset:
        pin = pin + motor_data_obj.calc_pin(motor[0], motor[1])

    # Add extra (non-motor) active power
    pin = pin + p_extra[0]

    return pin


def qin_tot_calc(motor_data_obj, motor_list_obj, p_extra):
    """Calculate total apparent power (Qin) for an installation.

    Qin includes motor contributions plus the reactive part of any extra load.
    """
    qin = 0

    for motor in motor_list_obj.dataset:
        qin = qin + motor_data_obj.calc_qin(motor[0], motor[1])

    # Add reactive part of the extra load (P_extra * tan(arccos(pf_extra)))
    qin = qin + p_extra[0] * math.tan(math.acos(p_extra[1]))

    return qin


def pf_calc(p, q):
    """Compute power factor (cosφ) from active (P) and apparent (Q) powers.

    The function uses the relation cosφ = cos(atan(Q/P)).
    """
    pf = math.cos(math.atan(q / p))

    return pf


def comp_calc(Pin, Qin, pf):
    """Decide and calculate reactive compensation required to reach 0.95 pf.

    Returns q_comp (kVA). If no compensation is needed returns 0.
    """
    q_comp = 0

    if pf_check(pf):
        # Already at 0.95 — nothing to do
        print("No compensation needed.\n")
        return q_comp
    else:
        # Calculate required Qin for target pf=0.95 and return difference
        print("calculating compensation....")

        qin_tot = Pin * math.tan(math.acos(0.95))

        q_comp = qin_tot - Qin

        print("Q compensation is", round(q_comp, 3), "kVA\n")

        return q_comp


def sync_factor_calc(Pin, Qin, sf):
    """Apply a synchronizing/diversity factor to Pin and Qin.

    Returns a two-item list [Pin_scaled, Qin_scaled].
    """
    s_sync = [Pin * sf, Qin * sf]

    return s_sync


def pf_check(pf):
    """Check whether installation PF equals the target (0.95).

    This function prints a helpful message and returns True when no action is
    required (pf == 0.95), otherwise False.
    """
    if not pf == 0.95:
        avg_pf = (pf + 0.95) / 2
        print("cosφ need's to be 0.95")
        print("so, average cosφ for the installation is", round(avg_pf, 3), "\n")
        return False
    else:
        return True


def scale_factor_calc(pin, scale):
    """Apply a scale to a base power value.

    Historically the project expected `scale` to be an incremental factor
    (e.g. 0.1 meaning +10%), so the function returns pin * (scale + 1).
    """

    scaled_value = pin * (scale + 1)

    return scaled_value