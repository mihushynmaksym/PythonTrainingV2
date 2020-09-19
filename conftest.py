import pytest
from fixture.application import Application

fixture = None


@pytest.fixture  # init fixture one time
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    login = request.config.getoption("--login")
    password = request.config.getoption("--password")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url, login=login, password=password)
    else:
        if not fixture.is_valid():  # check rule if web driver is running, if url is visible = True
            fixture = Application(browser=browser, base_url=base_url, login=login, password=password)
    fixture.session.ensure_login(login=login, password=password)  # check for login logic
    return fixture


@pytest.fixture(scope="session", autouse=True)  # destroy fixture for all session
def stop(request):
    def fin():
        fixture.session.ensure_logout()  # check for logout logic
        fixture.destroy()
    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost:8080/addressbook/index.php")
    parser.addoption("--login", action="store", default="")
    parser.addoption("--password", action="store", default="")
