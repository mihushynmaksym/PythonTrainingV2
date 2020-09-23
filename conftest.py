import pytest
import os.path
import jsonpickle
from fixture.application import Application

fixture = None
target = None


@pytest.fixture  # init fixture one time
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = jsonpickle.decode(f.read())
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'], login=target['login'],
                              password=target['password'])
    fixture.session.ensure_login(login=target['login'], password=target['password'])  # check for login logic
    return fixture


@pytest.fixture(scope="session", autouse=True)  # destroy fixture for all session
def stop(request):
    def fin():
        fixture.session.ensure_logout()  # check for logout logic
        fixture.destroy()
    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("json_"):
            test_data = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/{0}.json".format(file))) as f:
        return jsonpickle.decode(f.read())
