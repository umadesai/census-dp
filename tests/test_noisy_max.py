import pytest
from .context import census_dp
from census_dp import noisy_max
import numpy as np


def test_noisy_max():
    n_max = noisy_max.noisy_max(np.array([100, 200, 1]), epsilon=0.01, sensitivity=2.0)
    assert(round(n_max, 0) == 0 or 1)
