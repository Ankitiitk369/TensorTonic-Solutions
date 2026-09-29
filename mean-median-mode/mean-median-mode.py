from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    if not x:
        return {"mean": None, "median": None, "mode": None}
        
    # Calculate mean and median using numpy
    mean_val = float(np.mean(x))
    median_val = float(np.median(x))
    
    # Calculate mode with tie-breaking logic
    counter = Counter(x)
    max_frequency = max(counter.values())
    
    # Filter all items matching the max frequency and pick the smallest
    modes = [k for k, v in counter.items() if v == max_frequency]
    mode_val = float(min(modes))
    
    return {
        "mean": mean_val,
        "median": median_val,
        "mode": mode_val
    }
