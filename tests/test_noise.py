from .context import census_dp
from census_dp import noise


def test_laplace_mech():
    total = 0
    for i in range(1000):
        total += noise.laplace_mech(mu=0, epsilon=2, sensitivity=1)
    k = total/1000.0
    assert(round(k, 1) == 0)


def test_geometric_mech():
    total = 0
    for i in range(1000):
        total += noise.geometric_mech(0, 1)
    k = total/1000.0
    assert(round(k, 1) == 0)
