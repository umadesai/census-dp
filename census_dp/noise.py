import numpy as np


def laplace_mech(mu, epsilon, sensitivity=1.0):
    """Implementation of the Laplace Mechanism that adds Laplacian-distributed noise to a function.
　
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


def geometric_mechanism(true_answer, budget, sensitivity, prng):
    """ Implementation of the Geometric Mechanism
  　
    Args:
      true_answer (float or numpy array): the true answer
      budget (float): the privacy budget to use
      sensitivity (int): the sensitivity of the query
      addition or deletion of one person from the database
      must change the query answer vector by an integer amount
      prng: a numpy random number generator
    """
    shape = np.shape(true_answer)
    epsilon = budget / float(sensitivity)
    p = 1 - np.exp(-epsilon)
    x = prng.geometric(p, size=shape) - 1
    y = prng.geometric(p, size=shape) - 1
    return x-y + true_answer
