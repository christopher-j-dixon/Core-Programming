import matplotlib.pyplot as plt
import math as ma
import pylab as pl

def babylonian_square_root(a, e, x0):
    """
    Calculate the square root of a positive number using the Babylonian method.
    
    Parameters:
    a (float): The number to find the square root of, must be positive.
    e (float): The desired level of accuracy, must be positive.
    x0 (float): The initial guess for the square root.
    
    Returns:
    tuple: The approximate square root and the number of iterations.
    """
    
    assert a > 0 and e > 0, "Both a and e must be positive numbers."
    
    x = [x0]
    n = 0
    
    while abs(x[n]**2 - a) >= e:
        x.append(0.5 * (x[n] + a / x[n]))
        n += 1
    
    return x[n], n

def babylonian_square_root_list(a, e, x0):
    """
    Calculate the square root of a positive number using the Babylonian method and return the list of approximations.
    
    Parameters:
    a (float): The number to find the square root of, must be positive.
    e (float): The desired level of accuracy, must be positive.
    x0 (float): The initial guess for the square root.
    
    Returns:
    list: A list of successive approximations to the square root of a.
    """
    
    assert a > 0 and e > 0, "Both a and e must be positive numbers."
    
    x = [x0]
    n = 0
    
    while abs(x[n]**2 - a) >= e:
        x.append(0.5 * (x[n] + a / x[n]))
        n += 1
    
    return x

def babylonian_square_root_plot(a, e, x0):
    """
    Calculate and plot the approximations of the square root of a positive number using the Babylonian method.
    
    Parameters:
    a (float): The number to find the square root of, must be positive.
    e (float): The desired level of accuracy, must be positive.
    x0 (float): The initial guess for the square root.
    """
    
    assert a > 0 and e > 0, "Both a and e must be positive numbers."
    
    x = [x0]
    z = [0]
    n = 0
    
    while abs(x[n]**2 - a) >= e:
        x.append(0.5 * (x[n] + a / x[n]))
        n += 1
        z.append(n)
    
    plt.scatter(z, x)
    plt.plot(z, [pl.sqrt(a)] * len(z), 'r')
    
    plt.legend(["$x_n$", f"$\\sqrt{{{a}}}$"])
    plt.xlabel("n")
    plt.ylabel("Approximation")
    plt.title("Babylonian Method Square Root Approximation")
    plt.grid(True)
    plt.show()

babylonian_square_root_plot(20000, 1e-10, 1)
