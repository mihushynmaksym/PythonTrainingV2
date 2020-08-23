from fixture.application import Application
from model.group import Group
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_new_group(app):
    app.session.login(login='admin', password='secret')
    app.group.create(Group(name='param1', header='param2', footer='param3'))
    app.session.logout()
