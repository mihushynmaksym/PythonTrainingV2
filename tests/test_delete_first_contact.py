from model.contact import Contact


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
    app.contact.delete()
