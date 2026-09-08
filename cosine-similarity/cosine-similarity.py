import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    norm_x = 0
    norm_y = 0
    result = 0
    for i in range(len(a)):
        norm_x += a[i]*a[i]
        norm_y += b[i]*b[i]

    norm_x = np.sqrt(norm_x)
    norm_y = np.sqrt(norm_y)
    if norm_x == 0 or  norm_y == 0:
        return 0.0

    for i in range(len(a)):
        result +=a[i]*b[i]

    return float( result / ((norm_x) * norm_y ) )
        