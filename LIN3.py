import numpy as np
import sympy as sp

def gram_schmidt_np(V):
    """
    Perform Gram-Schmidt orthogonalization on a set of vectors.

    Parameters:
    ----------
    V : list of numpy.ndarray
        The input list of vectors to be orthogonalized.

    Returns:
    -------
    list of numpy.ndarray
        The orthogonalized and normalized list of vectors.

    Raises:
    ------
    ValueError
        If the input is not a list of vectors or if any vector is not a valid numpy array.
    """
    if not isinstance(V, list) or not all(isinstance(v, np.ndarray) for v in V):
        raise ValueError("Input must be a list of numpy arrays.")

    for v in V:
        if not isinstance(v, np.ndarray):
            raise ValueError("All elements in the input list must be numpy arrays.")
        if len(v) != len(V[0]):
            raise ValueError("All vectors must have the same length.")

    def unit_vector(v):
        norm = np.linalg.norm(v)
        if norm == 0:
            return v
        return v / norm

    A = []
    A.append(unit_vector(V[0]))

    for i in range(1, len(V)):
        u = V[i]
        for j in range(i):
            u = u - np.dot(V[i], A[j]) * A[j]
        A.append(unit_vector(u))

    return A

def gram_schmidt_sp(V):
    """
    Perform the Gram-Schmidt process to construct an orthonormal set of vectors.

    Parameters:
    ----------
    V : sympy.Matrix
        The input square matrix where columns represent the set of n-dimensional vectors.

    Returns:
    -------
    sympy.Matrix
        The matrix with orthonormal vectors as rows.
    
    Raises:
    ------
    ValueError
        If the input is not a square sympy.Matrix.
    """
    if not isinstance(V, sp.Matrix):
        raise ValueError("Input must be a sympy.Matrix.")
    if V.rows != V.cols:
        raise ValueError("Input matrix must be square.")
    
    n = V.cols
    W = sp.zeros(n, n)
    
    for i in range(n):
        vi = V[:, i]
        wi = vi
        
        for j in range(i):
            wj = W[:, j]
            proj = (vi.dot(wj) / wj.dot(wj)) * wj if wj.norm() != 0 else sp.zeros(n, 1)
            wi -= proj
        
        if wi.norm() != 0:
            wi = wi / wi.norm()
        
        W[:, i] = wi
    
    return W.transpose()