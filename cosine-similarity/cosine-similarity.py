import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    
    A = np.linalg.norm(a)
    B = np.linalg.norm(b)
    if A ==0 or B == 0:
        return 0.00
    dot = np.dot(a,b)
    similarity = dot/(A*B)
    return float(similarity)
    pass