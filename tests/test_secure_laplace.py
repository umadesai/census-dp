from .context import census_dp
from census_dp import secure_laplace


def test_secure_laplace_mech():
    query_sensitivity = 0.1
    privacy_budget = 10
    total = 0
    for i in range(1000):
        total += secure_laplace.secure_laplace_mech(query_sensitivity/privacy_budget)
    k = total/1000.0
    assert(k < 0.1 and k > -0.1)
