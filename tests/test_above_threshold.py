import pytest
from .context import census_dp
from census_dp import above_threshold


@pytest.mark.parametrize("T, forward, res", [
    (50, False, 7.0),
    (50, True, 0.0),
])
def test_above_threshold(T, forward, res):
    querylist = [100, 1, 2, 3, 4, 5, 6, 99]
    epsilon = 1
    sensitivity = 1.0
    val = above_threshold.above_threshold(querylist, T, epsilon, sensitivity, forward)
    assert(round(val, 1) == res)
