import pytest
from .context import census_dp
from census_dp import geometric


@pytest.mark.parametrize("mu, budget, res", [
    (0, 2, 0),
    (1, 4, 1),
    (2, 5, 2),
    (3, 3, 3),
])
def test_geometric_mech(mu, budget, res):
    total = 0
    for i in range(1000):
        total += geometric.geometric_mech(mu, budget)
    k = total/1000.0
    assert(round(k, 1) == res)
