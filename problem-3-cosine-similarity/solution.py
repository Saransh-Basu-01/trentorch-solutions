import numpy as np


def solve(a, b):
    """Implement Cosine Similarity from the mathematical contract in README.md."""
    a=np.asarray(a)
    b=np.asarray(b)
    dot_prod=np.dot(a,b)
    mag_a=np.linalg.norm(a)
    mag_b=np.linalg.norm(b)
    if mag_a==0 or mag_b==0:
        return 0
    return dot_prod/(mag_a*mag_b)
