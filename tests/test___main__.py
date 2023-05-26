import pytest
import runpy

from unittest import mock


@mock.patch("pycrawl.cli.main")
def test___main__(mock_main):
    mock_main.return_value = 42
    with pytest.raises(SystemExit) as e:
        runpy.run_module("pycrawl", run_name="__main__")
    assert e.type == SystemExit
    assert e.value.code == 42
