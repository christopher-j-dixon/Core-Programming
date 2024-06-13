import matplotlib.pyplot as plt
import numpy as np

def secant_method(f, x0, x1, tol, kmax):
    """
    Find the root of a function using the secant method.

    Parameters:
    ----------
    f : function
        The function for which we are trying to find a root.
    x0 : float
        Initial guess for the root.
    x1 : float
        Second guess for the root.
    tol : float
        The tolerance for the convergence criterion.
    kmax : int
        The maximum number of iterations.

    Returns:
    -------
    tuple
        xN : float
            The estimated root.
        eN : float
            The error estimate.
        N : int
            The number of iterations performed.
    """
    
    if tol <= 0:
        raise ValueError("Tolerance (tol) must be positive.")
    if kmax <= 0:
        raise ValueError("Maximum iterations (kmax) must be positive.")
    if x0 == x1:
        raise ValueError("Initial guesses (x0 and x1) must be different.")

    k = 0
    x = [x0, x1]
    ek = abs((x[k + 1] - x[k]) / x[k + 1])

    while (ek >= tol) and (k <= kmax):
        k += 1
        x_new = x[k] - ((x[k] - x[k - 1]) / (f(x[k]) - f(x[k - 1]))) * f(x[k])
        x.append(x_new)
        ek = abs((x[k + 1] - x[k]) / x[k + 1])

        if k > kmax:
            raise ArithmeticError("Maximum number of iterations exceeded.")
    
    xN = x[-1]
    eN = ek
    N = k

    return xN, eN, N

def secant_method_list(f, x0, x1, tol, kmax):
    """
    Find the root of a function using the secant method and return a list of iterations.

    Parameters:
    ----------
    f : function
        The function for which we are trying to find a root.
    x0 : float
        Initial guess for the root.
    x1 : float
        Second guess for the root.
    tol : float
        The tolerance for the convergence criterion.
    kmax : int
        The maximum number of iterations.

    Returns:
    -------
    list of tuples
        Each tuple contains an approximation of the root and the corresponding function value.
    """
    
    if tol <= 0:
        raise ValueError("Tolerance (tol) must be positive.")
    if kmax <= 0:
        raise ValueError("Maximum iterations (kmax) must be positive.")
    if x0 == x1:
        raise ValueError("Initial guesses (x0 and x1) must be different.")

    k = 0
    x = [x0, x1]
    ek = abs((x[1] - x[0]) / x[1])
    r = [(x[0], f(x[0]))]

    while ek >= tol and k < kmax:
        k += 1
        x_new = x[k] - ((x[k] - x[k - 1]) / (f(x[k]) - f(x[k - 1]))) * f(x[k])
        x.append(x_new)
        ek = abs((x[k + 1] - x[k]) / x[k + 1])
        r.append((x_new, f(x_new)))

        if k >= kmax:
            raise ArithmeticError("Maximum number of iterations exceeded, no roots found.")
    
    return r

def f(x):
    return (x**3 - x**2 + 2*x + 1) / (3*x**2 + 2)

x = np.linspace(-4, 3, num=1000)
y = f(x)

plt.figure(figsize=(20, 10))
plt.xlim([-3, 2])
plt.ylim([-1.5, 1])
plt.plot(x, y, label='f(x)')

z = secant_method_list(f, -2, 1, 1e-10, 100)
print(z)

for n in range(4):
    plt.plot(z[n][0], z[n][1], "o")
    plt.annotate(f"z{n}", (z[n][0], z[n][1]))
    
    x_line = [z[n][0], z[n + 1][0]]
    y_line = [z[n][1], z[n + 1][1]]
    plt.plot(x_line, y_line, label=f"Secant line {n}")

plt.axhline(y=0, color="black", label="y=0")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function f(x) and Secant Method Approximations")
plt.legend()
plt.grid(True)
plt.savefig('outputimage.png')
plt.show()
