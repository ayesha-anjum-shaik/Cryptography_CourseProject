# Importing the required libraries
import numpy as np
import matplotlib.pyplot as plt

def logistic_key(xinit, yinit, zinit, num_steps):
    """
    This function returns 3 lists of pseudo-random
    numbers generated using logistic system of differential
    equations.

    Parameters:
        xinit: float
            initial value of x
        yinit: float
            initial value of y
        zinit: float
            initial value of z
        num_steps: int
            number of keys required
            in a single list
    
    Returns:
        3 lists with pseudo-random numbers
        as their elements
    """

    # Initializing dt to a small value
    dt = 0.01

    # Initializing 3 empty lists
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)

    # Initializing initial values
    xs[0], ys[0], zs[0] = (xinit, yinit, zinit)

    # Initializing constants
    s = 10
    r = 28
    b = 2.667

    # System of equations
    for i in range(num_steps):
        xs[i + 1] = xs[i] + (s * (ys[i] - xs[i]) * dt)
        ys[i + 1] = ys[i] + ((xs[i] * (r - zs[i]) - ys[i]) * dt)
        zs[i + 1] = zs[i] + ((xs[i] * ys[i] - b * zs[i]) * dt)

    return xs, ys, zs

