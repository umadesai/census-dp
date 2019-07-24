import pytest
from .context import census_dp
from census_dp import mse, laplace
import numpy as np


def test_mse():
    mu = 0.0
    error = mse.mse(mu, laplace.laplace_mech, mu, 1, 1)
    assert(round(error, 1) == 2.0)
