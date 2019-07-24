import pytest
from .context import census_dp
from census_dp import dp_mean


def test_dp_mean():
    mean = dp_mean.dp_mean(10, 10, 4, 2, top_sen=1.0, bot_sen=1.0)
    assert(round(mean, 0) == 2)
