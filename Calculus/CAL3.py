
import numpy as np
import sympy as sym

def evalFn(n, x, y):
    """
    Evaluate the function based on the given inputs.

    Parameters:
    ----------
    n : int
        The degree of the function to evaluate.
    x : np.ndarray or float
        The x input values.
    y : np.ndarray or float
        The y input values.

    Returns:
    -------
    np.ndarray or float
        The evaluated function result.
    """
    if isinstance(x, np.ndarray) and isinstance(y, np.ndarray):
        if np.shape(x) != np.shape(y):
            raise ValueError("Shapes of x and y must be the same.")

        H = [np.array([[1, 1], [1, 1], [1, 1]])]
        H.append(x / 2 - y**2)

        for i in range(1, n):
            H.append(((2 * i * x * y) * H[i] - (2 * i + 1) * H[i - 1]) / (2 * i**2))

        return H[n]

    elif isinstance(x, (int, float)) and isinstance(y, (int, float)):
        F = np.zeros(n + 1)
        F[0] = 1
        F[1] = x / 2 - y**2

        for i in range(1, n):
            F[i + 1] = ((2 * i * x * y) * F[i] - (2 * i + 1) * F[i - 1]) / (2 * i**2)

        return float(F[n])
    else:
        raise ValueError("x and y must both be either np.ndarray or both int/float.")

def symbolicFn(n, x, y):
    """
    Evaluate the symbolic function based on the given inputs.

    Parameters:
    ----------
    n : int
        The degree of the function to evaluate. Must be a non-negative integer.
    x : sympy.core.symbol.Symbol
        The x variable.
    y : sympy.core.symbol.Symbol
        The y variable.

    Returns:
    -------
    sympy.Poly
        The evaluated polynomial.

    Raises:
    ------
    ValueError
        If n is not a non-negative integer or x and y are not sympy symbols.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError('Invalid n input! n must be a non-negative integer.')
    
    if not (isinstance(x, sym.core.symbol.Symbol) and isinstance(y, sym.core.symbol.Symbol)):
        raise ValueError('Invalid x or y input! x and y must be sympy symbols.')
    
    if n == 0:
        return sym.Poly(1, x, y, domain=sym.QQ)
    
    F = [1, x/2 - y**2]
    
    for i in range(1, n):
        F.append(((2*i*x*y)*F[i] - (2*i + 1)*F[i - 1]) / (2*i**2))
    
    return sym.Poly(F[n], x, y, domain=sym.QQ)

# Example usage:
x, y = sym.symbols('x y')
print(symbolicFn(3, x, y))

# Define symbols
x = sym.Symbol('x')
y = sym.Symbol('y')

# Define function G
G = 1 + x**2 * y**2

def S(x):
    """
    Compute the polynomial S(x) which is the integral of G with respect to y
    from y = x^2 to y = 1, and return it as a sympy polynomial in x.

    Parameters:
    ----------
    x : sympy.Symbol
        The variable of the polynomial.

    Returns:
    -------
    sympy.Poly
        The resulting polynomial.
    """
    integral = sym.integrate(G, (y, x**2, 1))
    return sym.Poly(integral, x, domain=sym.QQ)

def D(x, n):
    """
    Compute the nth derivative of the integral of G with respect to y from y = x^2 to y = 1,
    and return it as a sympy polynomial in x.

    Parameters:
    ----------
    x : sympy.Symbol
        The variable of the polynomial.
    n : int
        The order of the derivative.

    Returns:
    -------
    sympy.Poly
        The resulting polynomial after differentiation.
    """
    integral = sym.integrate(G, (y, x**2, 1))
    derivative = sym.diff(integral, (x, n))
    return sym.Poly(derivative, x, domain=sym.QQ)

def T(a):
    """
    Compute the definite integral of the integral of G with respect to y from y = x^2 to y = 1,
    integrated with respect to x from 0 to a, and return it as a sympy polynomial in x.

    Parameters:
    ----------
    a : sympy.Symbol
        The upper limit of the integral with respect to x.

    Returns:
    -------
    sympy.Poly
        The resulting polynomial after integration.
    """
    integral = sym.integrate(G, (y, x**2, 1))
    definite_integral = sym.integrate(integral, (x, 0, a))
    return sym.Poly(definite_integral, x, domain=sym.QQ)

# Example usage:
x, y = sym.symbols('x y')
a = sym.Symbol('a')
print(S(x))
print(D(x, 2))
print(T(a))
