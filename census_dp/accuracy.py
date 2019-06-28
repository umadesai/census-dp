import numpy as np
import matplotlib.pyplot as plt


def mse(true_answer, function_name, *params):
    """true_answer is either a scalar or numpy array"""
    niterations = 100_000
    return sum(np.sum((true_answer - function_name(*params))**2) for x in range(niterations)) / float(niterations)


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


def plot_roc(accuracy_df):
    accuracy_df.plot.scatter('episolon', 'accuracy')
    plt.show()
