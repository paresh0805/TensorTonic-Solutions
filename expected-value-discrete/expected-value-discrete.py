import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x=np.array(x,dtype=float)
    p=np.array(p,dtype=float)
    if np.allclose(np.sum(p),1):
        return np.sum(x*p)
    else : raise ValueError("Probabilities don't sum to 1")
        
