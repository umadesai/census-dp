import pytest
from .context import census_dp
from census_dp import laplace


@pytest.mark.parametrize("mu, epsilon, sensitivity, res", [
    (0, 2, 1, 0),
    (1, 4, 1, 1),
    (2, 3, 1, 2),
    (3, 5, 1, 3),
])
def test_laplace_mech(mu, epsilon, sensitivity, res):
    total = 0
    for i in range(1000):
        total += laplace.laplace_mech(mu=mu, epsilon=epsilon, sensitivity=sensitivity)
    k = total/1000.0
    assert(round(k, 1) == res)
