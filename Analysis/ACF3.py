import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import sympy

def estimate_pi_monte_carlo(Ntotal):
    """
    Estimate the value of π using the Monte Carlo method.

    Parameters:
    ----------
    Ntotal : int
        The total number of random points to generate.

    Returns:
    -------
    sympy.Rational
        The estimated value of π as a sympy Rational.
    """
    if Ntotal <= 0 or not isinstance(Ntotal, int):
        raise ValueError("Ntotal must be a positive integer.")
    
    x_inside = []
    y_inside = []

    for _ in range(Ntotal):
        x = rnd.uniform(-1, 1)
        y = rnd.uniform(-1, 1)
        
        if np.sqrt(x**2 + y**2) <= 1:
            x_inside.append(x)
            y_inside.append(y)
    
    Ndisc = len(x_inside)
    
    return sympy.Rational(4 * Ndisc / Ntotal)

def draw_monte_carlo(Ntotal):
    """
    Draw a Monte Carlo simulation for estimating π.

    Parameters:
    ----------
    Ntotal : int
        The total number of random points to generate.
    """
    if Ntotal <= 0 or not isinstance(Ntotal, int):
        raise ValueError("Ntotal must be a positive integer.")
    
    x = []
    y = []
    x_inside = []
    y_inside = []

    for _ in range(Ntotal):
        xi = rnd.uniform(-1, 1)
        yi = rnd.uniform(-1, 1)
        x.append(xi)
        y.append(yi)
        
        if np.sqrt(xi**2 + yi**2) <= 1:
            x_inside.append(xi)
            y_inside.append(yi)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), subplot_kw={'aspect': 'equal'})

    # Plot the unit circle
    ax1.set_xlim(-1, 1)
    ax1.set_ylim(-1, 1)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.add_patch(Rectangle((-1, -1), 2, 2, color='r', fill=True))
    ax1.add_patch(Circle((0, 0), 1, color='g', fill=True))
    ax1.set_title('Unit Circle')

    # Scatter plot
    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1, 1)
    ax2.scatter(x, y, color='r', label='Outside Circle')
    ax2.scatter(x_inside, y_inside, color='g', label='Inside Circle')
    ax2.add_patch(Circle((0, 0), 1, color='b', fill=False))
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_title('Scatter Plot')
    ax2.legend()

    plt.show()
    fig.savefig('outputimage.png')

draw_monte_carlo(250)

import numpy as np
import sympy as sym

def estimate_pi_chudnovsky(n):
    """
    Estimate the value of π using the Chudnovsky algorithm.

    Parameters:
    ----------
    n : int
        The number of terms to include in the series.

    Returns:
    -------
    float
        The estimated value of π with high precision.
    """
    if n < 0 or not isinstance(n, int):
        raise ValueError("n must be a non-negative integer.")
    
    c = 0
    for k in range(n + 1):
        Nom = (-1)**k * sym.factorial(6 * k) * (13591409 + 545140134 * k)
        Dom = sym.factorial(3 * k) * sym.factorial(k)**3 * (640320**(3 * k + sym.Rational(3/2)))
        c += Nom / Dom
    
    pi_estimate = (12 * c)**-1
    return pi_estimate.evalf(1000)

# Example usage:
print(estimate_pi_chudnovsky(10))
