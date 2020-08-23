from application import Application
from group import Group
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_group(app):
    app.login(login='admin', password='secret')
    app.create_new_group(Group(name='param1', header='param2', footer='param3'))
    app.logout()
