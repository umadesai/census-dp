from .context import census_dp
from census_dp import noise
import pytest


@pytest.mark.parametrize("mu, epsilon, sensitivity, res", [
    (0, 2, 1, 0),
    (1, 4, 1, 1),
    (2, 3, 1, 2),
    (3, 5, 1, 3),
])
def test_laplace_mech(mu, epsilon, sensitivity, res):
    total = 0
    for i in range(1000):
        total += noise.laplace_mech(mu=mu, epsilon=epsilon, sensitivity=sensitivity)
    k = total/1000.0
    assert(round(k, 1) == res)


@pytest.mark.parametrize("mu, budget, res", [
    (0, 2, 0),
    (1, 4, 1),
    (2, 5, 2),
    (3, 3, 3),
])
def test_geometric_mech(mu, budget, res):
    total = 0
    for i in range(1000):
        total += noise.geometric_mech(mu, budget)
    k = total/1000.0
    assert(round(k, 1) == res)
