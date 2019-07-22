import numpy as np
from laplace import laplace_mech


def l1_norm(epsilon, mu, n=1000, mechanism=laplace_mech):
    """Takes the average l1 error of the input mechanism on an array over n samples.
　
    Args:
      epsilon (int): the privacy budget
      mu (float or numpy array): the true answer
      n (int): number of samples
      mechanism (function): noise injection mechanism
    """
    total = 0
    for i in range(n):
        noisy_arr = mechanism(mu, epsilon, sensitivity=1.0)
        accuracy = 1 - (np.linalg.norm(noisy_arr-mu, 1)/(2*noisy_arr.shape[1]))
        total += accuracy
    return total/n
