"""
Noise injection algorithms
"""

import numpy as np
from typing import Union


def laplace_mech(mu: Union[float, np.ndarray], epsilon: int, sensitivity: float = 1.0):
    """
    Implementation of the Laplace Mechanism that adds
    Laplacian-distributed noise to a function.

    Args:
      mu (float or numpy array): the true answer
      epsilon (int): the privacy budget
      sensitivity (float): the global sensitivity of the query
    """
    eps = epsilon/float(sensitivity)
    scale = 1/eps
    np_shape = np.shape(mu)
    shape = None if np_shape == () else np_shape
    z = np.random.laplace(0.0, scale=scale, size=shape)
    return mu + z


def geometric_mech(mu: Union[float, np.ndarray], epsilon: int, sensitivity: float = 1.0):
    """Implementation of the Geometric Mechanism

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
