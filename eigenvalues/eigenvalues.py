import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """Return the real eigenvalues in ascending order."""
    # Write code here
    matrix = np.asarray(matrix, dtype=float)
    l = np.linalg.eigvals(matrix)
    return np.sort(l.real)