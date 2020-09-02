import pytest
from fixture.application import Application

fixture = None


@pytest.fixture  # init fixture one time
def app():
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():  # check rule if web driver is running, if url is visible = True
            fixture = Application()
    fixture.session.ensure_login(login='admin', password='secret')  # check for login logic
    return fixture


@pytest.fixture(scope="session", autouse=True)  # destroy fixture for all session
def stop(request):
    def fin():
        fixture.session.ensure_logout()  # check for logout logic
        fixture.destroy()
    request.addfinalizer(fin)
