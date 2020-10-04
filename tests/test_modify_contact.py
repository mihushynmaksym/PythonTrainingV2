from model.contact import Contact
import random


def test_modify_contact(app, db):
    contact_value = Contact(firstname='firstname1',
                      middlename='midlename2',
                      lastname='lastname3',
                      nickname='nickname4',
                      title='title5',
                      company='company6',
                      address='adress7',
                      home='home8',
                      mobile='mobile9',
                      work='work10',
                      fax='fax11',
                      email='email12',
                      email2='email213',
                      email3='email314',
                      homepage='homepage15',
                      byear='1988',
                      ayear='2020',
                      adress2='adress218',
                      phone2='phone219',
                      notes='notes20')
    if len(db.get_contact_list()) == 0:  # precondition rule for test
        app.contact.create(contact_value)
    old_contacts = db.get_contact_list()
    contacts = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contacts.id, contact_value)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
