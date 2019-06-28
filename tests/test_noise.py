from .context import census_dp
# from census_dp import laplace_mech
import pytest


def test_laplace():
    total = 0
    for i in range(1000):
        total += census_dp.laplace_mech(x=0, budget=2, sensitivity=1)
    print(total/1000.0)
