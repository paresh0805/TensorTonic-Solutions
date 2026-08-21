import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    mean_x = np.mean(x)
    var = np.sum((x-mean_x)**2)/(len(x)-1);
    sd = np.sqrt(var)

    return var,sd