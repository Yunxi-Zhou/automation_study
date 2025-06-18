import pytest

@pytest.fixture(scope='function',autouse=True)
def goto_frame():
    print('go to dk_manage frame')