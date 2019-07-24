from laplace import laplace_mech


def dp_variance(mu_list, epsilon):
    """
    Compute a differentially private variance.
    """
    noisy_n = laplace_mech(mu_list.size, 0.3333333, 1.0)
    noisy_sum_sq = laplace_mech((mu_list * mu_list).sum(), 0.3333333, 100.0**2)
    noisy_sum = laplace_mech(mu_list.sum(), 0.33333333, 100.0)
    return noisy_sum_sq/noisy_n - (noisy_sum/noisy_n)**2
