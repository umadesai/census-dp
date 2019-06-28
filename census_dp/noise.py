"""
Noise injection algorithms
"""

import numpy as np


def laplace_mech(mu, epsilon, sensitivity=1.0):
    """Implementation of the Laplace Mechanism that adds
    Laplacian-distributed noise to a function.
　
    Args:
      mu (float or numpy array): the true answer
      epsilon(int): the privacy budget
      sensitivity (float): the global sensitivity of the query
    """
    eps = epsilon/float(sensitivity)
    scale = 1/eps
    np_shape = np.shape(mu)
    shape = None if np_shape == () else np_shape
    z = np.random.laplace(0.0, scale=scale, size=shape)
    return mu + z


def geometric_mech(mu, budget, sensitivity=1.0, prng=np.random):
    """Implementation of the Geometric Mechanism
　
    Args:
      mu (float or numpy array): the true answer
      budget (float): the privacy budget to use
      sensitivity (float): the global sensitivity of the query
      prng: a numpy random number generator
    """
    shape = np.shape(mu)
    epsilon = budget/float(sensitivity)
    p = 1 - np.exp(-epsilon)
    x = prng.geometric(p, size=shape) - 1
    y = prng.geometric(p, size=shape) - 1
    return x-y + mu
