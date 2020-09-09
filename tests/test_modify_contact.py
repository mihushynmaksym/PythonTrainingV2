from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    contact_value = Contact(firstname='firstname',
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
                            notes='notes')
    if app.contact.count() == 0:  # precondition rule for test
        app.contact.create(contact_value)
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact_value.id = old_contact[index].id
    app.contact.modify_by_index(index, contact_value)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[index] = contact_value
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
