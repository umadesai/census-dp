import numpy as np
from laplace import laplace_mech


def noisy_max(answers: np.ndarray, epsilon: float, sensitivity: float):
    """ Implementation of the noisy max mechanism with gap using Laplace noise

    Given a set of queries, this mechanism will return the **index**, not the
    value, of the query that is probably largest.

    Args:
      answers (float or numpy array): the set of queries
      epsilon (float): the privacy budget
      sensitivity (float): the global sensitivity of the query
    """
    noisy_answers = laplace_mech(answers, epsilon/2.0, sensitivity)
    return noisy_answers.argmax()
