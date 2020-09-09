from model.contact import Contact


def test_create_new_contact(app):
    old_contacts = app.contact.get_contact_list()
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
    app.contact.create(contact_value)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact_value)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
