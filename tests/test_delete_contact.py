from model.contact import Contact
import random


def test_delete_random_contact(app, db):
    if len(db.get_contact_list()) == 0:   # precondition rule for test
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
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
