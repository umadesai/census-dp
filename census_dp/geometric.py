import numpy as np
from typing import Union


def geometric_mech(mu: Union[float, np.ndarray], epsilon: int, sensitivity: float = 1.0):
    """Implementation of the Geometric Mechanism. The Geometric Mechanism is a
    discrete variant of the Laplace Mechanism. It is useful when integer-valued
    output is desired.

    Args:
      mu (float or numpy array): the true answer
      epsilon (int): the privacy budget
      sensitivity (float): the global sensitivity of the query
    """
    shape = np.shape(mu)
    eps = epsilon/float(sensitivity)
    p = 1 - np.exp(-eps)
    x = np.random.geometric(p, size=shape) - 1
    y = np.random.geometric(p, size=shape) - 1
    return x-y + mu
