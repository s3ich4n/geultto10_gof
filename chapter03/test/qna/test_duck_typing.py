import pytest
from src.map_site import MapSite


def test_pass_will_run_normally():
    with pytest.raises(Exception):
        what = MapSite()
