"""
Accuracy measuring algorithms
"""
import numpy as np
from noise import laplace_mech


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


def avg_l1_laplace(epsilon, mu, n=1000):
    """Takes the average error of the laplace mechanism on an array over n samples.
　
    Args:
      epsilon (int): the privacy budget
      mu (float or numpy array): the true answer
      n (int): number of samples
    """
    total = 0
    for i in range(n):
        noisy_arr = laplace_mech(mu, epsilon, sensitivity=1.0)
        accuracy = 1 - (np.linalg.norm(noisy_arr-mu, 1)/(2*noisy_arr.shape[1]))
        total += accuracy
    return total/n
