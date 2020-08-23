import pytest
from fixture.application import Application


@pytest.fixture(scope='session')  # run all test in one session
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
