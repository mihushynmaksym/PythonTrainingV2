from model.contact import Contact
import time


def test_modify_contact(app):
    app.session.login(login='admin', password='secret')
    app.contact.modify(Contact(firstname='modify_name',
                               middlename='modify_midlename',
                               lastname='modify_lastname',
                               nickname='modify_nickname',
                               title='modify_title',
                               company='modify_company',
                               address='modify_adress',
                               home='modify_home',
                               mobile='modify_mobile',
                               work='modify_work',
                               fax='modify_fax',
                               email='modify_email',
                               email2='modify_email2',
                               email3='modify_email3',
                               homepage='modify_homepage',
                               byear='modify_byear',
                               ayear='modify_ayear',
                               adress2='modify_adress2',
                               phone2='modify_phone2',
                               notes='modify_notes'))
    app.session.logout()
    time.sleep(1)
