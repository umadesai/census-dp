import secrets
import math
import numpy as np


def secure_laplace_mech(scale):
    """
    Implementation of laplace mechanism using a CSPRNG from the secrets library.
    Secrets should be used in preference to the default pseudo-random number
    generator in most Python modules like numpy and random, which are designed
    for modelling and simulation, not security or cryptography.
    """
    secure_rand_gen = secrets.SystemRandom()
    # rand_num is the at least purportedly secure OpenSSL uniform RV generator on (0,1)
    uniform_rns = secure_rand_gen.uniform(0, 1)
    # inverse CDF transform (with a small trick): uniform -> laplace
    laplace_rns = np.sign(uniform_rns - 0.5) * scale * math.log(1. - 2. * abs(uniform_rns - 0.5))
    return laplace_rns
