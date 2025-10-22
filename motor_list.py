"""Installed motor list used by the example project.

Each entry is a two-item list: [motor_HP, quantity]. The list is consumed
by `MotorData` helper functions to compute power per motor type.
"""

motorList = [
    [2.00, 6],
    [3.00, 1],
    [3.00, 2],
    [5.50, 2],
    [1.00, 12],
    [5.50, 1],
    [1.50, 6],
    [7.50, 2],
    [10.00, 2],
    [3.00, 2],
    [1.00, 2],
    [10.00, 4],
    [10.00, 4],
    [1.00, 2],
    [7.50, 3],
    [4.00, 2],
    [5.50, 2],
    [1.00, 1],
    [0.50, 8],
    [5.50, 6],
    [10.00, 14],
    [5.50, 10],
    [4.00, 14],
    [50.00, 2],
    [5.50, 15],
    [10.00, 1],
    [1.00, 16],
    [5.50, 16],
    [1.50, 7],
    [7.50, 25],
    [10.00, 4],
    [30.00, 2],
    [3.00, 10],
    [0.50, 20],
    [10.00, 5],
    [5.50, 3],
    [1.50, 2],
    [7.50, 4],
    [75.00, 1],
    [3.00, 5],
    [5.50, 2],
    [15.00, 1],
    [15.00, 3],
    [5.50, 2],
    [10.00, 1],
    [15.00, 1],
    [30.00, 1],
    [5.50, 1],
    [3.00, 4],
    [5.50, 1],
    [5.50, 6],
]

class MotorList:
    """Simple wrapper class that exposes the installed motor dataset.

    The class stores the provided dataset on `.dataset` so the rest of the
    code can iterate over installed motor entries as `[hp, quantity]`.
    """

    def __init__(self, dataset):
        self.dataset = dataset
