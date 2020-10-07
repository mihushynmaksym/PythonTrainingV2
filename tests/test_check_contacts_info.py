from model.contact import Contact


def test_modify_contact(app, db):
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
    if len(db.get_contact_list()) == 0:  # precondition rule for test
        app.contact.create(contact_value)
    contact_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contact_ui)):
        assert contact_ui[i].firstname == contact_db[i].firstname
        assert contact_ui[i].lastname == contact_db[i].lastname
        assert contact_ui[i].address == contact_db[i].address
        assert contact_ui[i].all_emails_from_home_page == app.contact.merge_email_like_on_home_page(contact_db[i])
        assert contact_ui[i].all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_db[i])
