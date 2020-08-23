from fixture.application import Application
from model.contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_new_contact(app):
    app.session.login(login='admin', password='secret')
    app.contact.create(Contact(firstname='firstname',
                               middlename='midlename',
                               lastname='lastname',
                               nickname='nickname',
                               title='title',
                               company='company',
                               address='adress',
                               home='home',
                               mobile='mobile',
                               work='work',
                               fax='fax',
                               email='email',
                               email2='email2',
                               email3='email3',
                               homepage='homepage',
                               byear='byear',
                               ayear='ayear',
                               adress2='adress2',
                               phone2='phone2',
                               notes='notes'))
    app.session.logout()
