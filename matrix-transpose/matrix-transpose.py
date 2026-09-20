import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    if not A:
        return []

    # 2. Dimensions Gathering
    num_rows = len(A)
    num_cols = len(A[0])

    # 3. Transposition Core (Nested List Comprehension)
    return np.array(
        [[A[i][j] for i in range(num_rows)] for j in range(num_cols)]
    )
    pass
