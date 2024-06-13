import math as ma

def scalar_product(v1, v2):
    """
    Calculate the scalar (dot) product of two vectors.

    Parameters:
    ----------
    v1 : tuple
        An n-dimensional vector represented by a tuple with n items: (a1, a2, ..., an).
    v2 : tuple
        An n-dimensional vector represented by a tuple with n items: (b1, b2, ..., bn).

    Returns:
    -------
    float
        The scalar (dot) product of the two vectors.
    """
    
    # Raise a ValueError if the parameters (v1 or v2) are integers or floats.
    if isinstance(v1, (int, float)) or isinstance(v2, (int, float)):
        raise ValueError("This function accepts tuple parameters only.")
    
    # Raise a ValueError if the input are not tuples of equal length.
    if len(v1) != len(v2):
        raise ValueError("Vector 1 (v1) and Vector 2 (v2) do not have the same length and therefore are different dimensions!")
    
    dot_product = sum(v1[i] * v2[i] for i in range(len(v1)))
    
    return dot_product

import math as ma

def vector_perpendicular(P, Q):
    """
    Returns a vector perpendicular to the line passing through points P and Q.

    Parameters:
    ----------
    P : tuple
        A 2-dimensional point represented by a tuple: (p1, p2).
    Q : tuple
        A 2-dimensional point represented by a tuple: (q1, q2).

    Returns:
    -------
    tuple
        A vector perpendicular to the line passing through points P and Q.
    """
    
    # Compute a vector that is perpendicular to the vector from point P to Q.
    perpendicular_vector = (P[1] - Q[1], Q[0] - P[0])
    
    return perpendicular_vector

import math as ma

def intersection_lines(L1, L2):
    """
    Returns the point at which line one (L1) and line two (L2) intersect.

    Parameters:
    ----------
    L1 : tuple
        Line one, represented by a tuple: ((a1, c1), (b1, d1)).
    L2 : tuple
        Line two, represented by a tuple: ((a2, c2), (b2, d2)).

    Returns:
    -------
    tuple
        The coordinates (x, y) of the intersection point.
    """
    # Extracting points and direction vectors
    P1, v1 = L1
    P2, v2 = L2
    a1, c1 = P1
    b1, d1 = v1
    a2, c2 = P2
    b2, d2 = v2

    # Check if lines are parallel by comparing direction vectors
    if b1 * d2 == b2 * d1:
        raise ValueError("Lines one and two (L1 and L2) are parallel!")

    # Compute s value at the intersection of the two lines
    s = ((b2 * c1) - (b2 * c2) - (d2 * a1) + (d2 * a2)) / ((b1 * d2) - (b2 * d1))

    # Compute the coordinates of the intersection of lines one and two (L1 and L2)
    x = a1 + s * b1
    y = c1 + s * d1

    return (x, y)