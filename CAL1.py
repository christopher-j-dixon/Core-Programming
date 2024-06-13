import math as ma
import pylab as pl
import matplotlib.pyplot as plt

def bernoulli(m):
    """
    Calculate the mth Bernoulli number.

    Parameters:
    ----------
    m : int
        The order of the Bernoulli number, must be an integer such that 0 ≤ m ≤ 12.

    Returns:
    -------
    float
        The mth Bernoulli number.
    """
    Bm = 0
    
    # The double summation Bernoulli number formula for the mth Bernoulli number.
    for k in range(m + 1):
        for v in range(k + 1):
            Bm += (-1)**v * (v**m / (k + 1)) * ma.comb(k, v)
    
    return Bm

def pn(n, x):
    """
    Calculate the pn function using Bernoulli numbers.

    Parameters:
    ----------
    n : int
        The order of the pn function.
    x : float
        The variable x in the pn function.

    Returns:
    -------
    float
        The value of the pn function.
    """
    ans = 0
    
    for k in range(1, n + 1):
        ans += (bernoulli(2 * k) / ma.factorial(2 * k)) * (-4)**k * (1 - 4**k) * x**(2 * k - 1)
    
    return ans

def pn(n, x):
    """
    Calculate the pn function using Bernoulli numbers.

    Parameters:
    ----------
    n : int
        The order of the pn function.
    x : float
        The variable x in the pn function.

    Returns:
    -------
    float
        The value of the pn function.
    """
    ans = 0
    
    for k in range(1, n + 1):
        ans += (bernoulli(2 * k) / ma.factorial(2 * k)) * (-4)**k * (1 - 4**k) * x**(2 * k - 1)
    
    return ans

x = pl.linspace(-ma.pi / 3, ma.pi / 3, num=1000)

plt.plot(x, pl.tan(x), label="tan(x)")

for n in range(1, 4):
    plt.plot(x, pn(n, x), label=f"$p_{n}(x)$")

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Approximation of tan(x) using Bernoulli Polynomials")
plt.grid(True)
plt.show()
