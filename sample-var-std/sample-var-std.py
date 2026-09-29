import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Safeguard for empty or single-element lists where ddof=1 is undefined
    if len(x) <= 1:
        return {"variance": None, "standard_deviation": None}
        
    # Calculate variance and standard deviation with Bessel's correction (ddof=1)
    var_val = float(np.var(x, ddof=1))
    std_val = float(np.std(x, ddof=1))
    
    return {
        "variance": var_val,
        "standard_deviation": std_val
    }
