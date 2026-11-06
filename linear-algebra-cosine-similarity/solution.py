import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """
    a, b: 1-D vectors of equal length.

    Returns:
        the cosine of the angle between a and b, or 0.0 if either has
        zero length.
    """
    # TODO: Dot product divided by the product of the norms.
    dot_prod=np.dot(a,b)
    mag_a=np.linalg.norm(a)
    mag_b=np.linalg.norm(b)
    if mag_a==0 or mag_b==0:
        return 0
    return dot_prod/(mag_a*mag_b)
