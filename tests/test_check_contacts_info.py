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
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    contact_from_home_page = contact_list[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    all_phones = app.contact.merge_phones_like_on_home_page
    all_emails = app.contact.merge_email_like_on_home_page
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == all_emails(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == all_phones(contact_from_edit_page)

