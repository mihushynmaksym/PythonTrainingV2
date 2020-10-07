from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, db):
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
    group_value = Group(name='param1', header='param2', footer='param3')
    if len(db.get_group_list()) == 0:  # precondition rule for test
        app.group.create(group_value)
    elif len(db.get_contact_list()) == 0:
        app.contact.create(contact_value)
    contact_list = db.get_contact_list()
    group_list = db.get_group_list()
    contact = random.choice(contact_list)
    group = random.choice(group_list)
    if contact in db.get_contacts_not_in_group(Group(id='{0}'.format(group.id))):
        app.contact.add_contact_in_group(contact.id, group.id)
    assert contact in db.get_contacts_in_group(Group(id='{0}'.format(group.id)))


def test_dell_contact_in_group(app, db):
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
    group_value = Group(name='param1', header='param2', footer='param3')
    contact_list = db.get_contact_list()
    group_list = db.get_group_list()
    contact = random.choice(contact_list)
    group = random.choice(group_list)
    if len(db.get_group_list()) == 0:  # precondition rule for test
        app.group.create(group_value)
    elif len(db.get_contact_list()) == 0:
        app.contact.create(contact_value)
    elif contact not in db.get_contacts_in_group(Group(id='{0}'.format(group.id))):
        app.contact.add_contact_in_group(contact.id, group.id)
    app.contact.dell_contact_in_group(contact.id, group.id)
    assert contact in db.get_contacts_not_in_group(Group(id='{0}'.format(group.id)))
