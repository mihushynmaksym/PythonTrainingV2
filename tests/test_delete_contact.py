from model.contact import Contact
from random import randrange


def test_delete_first_contact(app):
    if app.contact.count() == 0:   # precondition rule for test
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
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
