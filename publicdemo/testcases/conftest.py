#fixture 固件
import pytest
from publicdemo.commons.yaml_util import clear_yaml

@pytest.fixture(scope='session', autouse=True)
def clears():
    clear_yaml()