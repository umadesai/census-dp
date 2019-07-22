import numpy as np
from laplace import laplace_mech


def matrix_mechanism(x, W, A, epsilon=1.0):
    ''' Implementation of the Matrix Mechanism.
    MM follows a “Select - Measure - Reconstruct” paradigm: given a set of
    target queries on which low accuracy is desired, these mechanisms Select an
    alternative set of queries, Measure estimated values of these alternative
    queries using the Laplace mechanism, and perform post-processing to
    optimally Reconstruct estimates to the original, target queries.

    Args:
      x ():
      W (): the query workload
      A (): the query strategy
      epsilon (float): the privacy budget
    '''
    # y = noisy answers to the queries in A
    y = laplace_mech(A, x, epsilon)
    # reconstruct from y to get x_hat
    # x_hat = computed estimate of x that minimizes squared error = pseudo-inverse(A)*y
    Aplus = np.linalg.pinv(A)
    x_hat = y @ Aplus
    # return noisy workload answers: W * x_hat
    return W @ x_hat
