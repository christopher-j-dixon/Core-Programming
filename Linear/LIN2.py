import numpy as np

def find_max_column_value(A, i, j):
    """
    Find the maximum value in a specified column from a starting row and its position.

    Parameters:
    ----------
    A : numpy.ndarray
        The input matrix.
    i : int
        The starting row index.
    j : int
        The column index.

    Returns:
    -------
    tuple
        A tuple containing the maximum value and its row position.
    """
    if i < 0 or i >= A.shape[0] or j < 0 or j >= A.shape[1]:
        raise IndexError("Row index i or column index j is out of bounds.")
    
    max_entry = np.max(A[i:, j])
    max_entry_row_position = np.where(A[:, j] == max_entry)[0][0]
    
    return max_entry, max_entry_row_position

def swap_rows(A, i, j):
    """
    Swap rows i and j in matrix A.

    Parameters:
    ----------
    A : numpy.ndarray
        The input matrix.
    i : int
        The index of the first row to swap.
    j : int
        The index of the second row to swap.

    Returns:
    -------
    numpy.ndarray
        The matrix with rows i and j swapped.
    """
    if i < 0 or i >= A.shape[0] or j < 0 or j >= A.shape[0]:
        raise IndexError("Row index out of bounds.")
    
    D = np.copy(A)
    D[[i, j], :] = D[[j, i], :]
    
    return D

def swap_cols(A, i, j):
    """
    Swap columns i and j in matrix A.

    Parameters:
    ----------
    A : numpy.ndarray
        The input matrix.
    i : int
        The index of the first column to swap.
    j : int
        The index of the second column to swap.

    Returns:
    -------
    numpy.ndarray
        The matrix with columns i and j swapped.
    """
    if i < 0 or i >= A.shape[1] or j < 0 or j >= A.shape[1]:
        raise IndexError("Column index out of bounds.")
    
    D = np.copy(A)
    D[:, [i, j]] = D[:, [j, i]]
    
    return D

import numpy as np

def gauss_elimination(A):
    """
    Perform Gaussian elimination on matrix A.

    Parameters:
    ----------
    A : numpy.ndarray
        The input matrix.

    Returns:
    -------
    numpy.ndarray
        The matrix after Gaussian elimination.
    """
    
    def less_than(a, b):
        return a if a < b else b
    
    if A.dtype.type is not np.float64:
        raise TypeError("'dtype' is not float64.")
    
    n, m = A.shape

    for j in range(less_than(n, m)):
        max_row = j + np.argmax(np.abs(A[j:, j]))
        
        if abs(A[max_row, j]) > abs(A[j, j]):
            A = swap_rows(A, max_row, j)
        
        for i in range(j + 1, n):
            if A[i, j] != 0:
                s = -A[i, j] / A[j, j]
                A[i] += s * A[j]
    
    return A

def find_max_column_value(A, i, j):
    """
    Find the maximum value in a specified column from a starting row and its position.

    Parameters:
    ----------
    A : numpy.ndarray
        The input matrix.
    i : int
        The starting row index.
    j : int
        The column index.

    Returns:
    -------
    tuple
        A tuple containing the maximum value and its row position.
    """
    if i < 0 or i >= A.shape[0] or j < 0 or j >= A.shape[1]:
        raise IndexError("Row index i or column index j is out of bounds.")
    
    max_entry = np.max(A[i:, j])
    max_entry_row_position = np.where(A[:, j] == max_entry)[0][0]
    
    return max_entry, max_entry_row_position

def swap_rows(A, i, j):
    """
    Swap rows i and j in matrix A.

    Parameters:
    ----------
    A : numpy.ndarray
        The input matrix.
    i : int
        The index of the first row to swap.
    j : int
        The index of the second row to swap.

    Returns:
    -------
    numpy.ndarray
        The matrix with rows i and j swapped.
    """
    if i < 0 or i >= A.shape[0] or j < 0 or j >= A.shape[0]:
        raise IndexError("Row index out of bounds.")
    
    D = np.copy(A)
    D[[i, j], :] = D[[j, i], :]
    
    return D

def add_row(A, i, j, s):
    """
    Add s times row j to row i in matrix A.

    Parameters:
    ----------
    A : numpy.ndarray
        The input matrix.
    i : int
        The index of the row to be updated.
    j : int
        The index of the row to be added.
    s : float
        The scalar multiplier.

    Returns:
    -------
    numpy.ndarray
        The updated matrix.
    """
    if i < 0 or i >= A.shape[0] or j < 0 or j >= A.shape[0]:
        raise IndexError("Row index out of bounds.")
    
    D = np.copy(A)
    D[i, :] += s * D[j, :]
    
    return D
