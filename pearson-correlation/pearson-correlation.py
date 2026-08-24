import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """Return the Pearson correlation matrix of X."""
    # Write code here
    matrix = np.asarray(X)
    centered = matrix - np.mean(matrix, axis=0)
    cov = centered.T @ centered/(matrix.shape[0]-1)
    sd = np.sqrt(np.diag(cov))
    d = np.outer(sd, sd)
    with np.errstate(divide="ignore", invalid='ignore'):
        return cov/d
    
    