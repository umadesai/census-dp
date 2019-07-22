import numpy as np


def mse(mu, algo, *params):
    """Runs the algorithm on the data over n iterations
    and computes the mean squared error.

    Args:
      mu (float or numpy array): the true answer
      algo (function): algorithm to run on the data
      *params: algo function params
    """
    n = 100_000
    return sum(np.sum((mu - algo(*params))**2) for x in range(n)) / float(n)
