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
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact_value)
    group = db.get_group_list()
    contact = db.get_contact_list()
    group_get_random = random.choice(group)
    old_contacts_in_group = db.get_contacts_in_group(group_get_random)
    contacts_is_not_group = []
    for i in contact:
        if i not in old_contacts_in_group:
            contacts_is_not_group.append(i)
    if len(contacts_is_not_group) != 0:
        contact_get_random = random.choice(contacts_is_not_group)
        app.contact.add_contact_in_group(contact_get_random.id, group_get_random.id)
        old_contacts_in_group.append(contact_get_random)
    else:
        create_contact = app.contact.create(contact)
        app.contact.add_contact_in_group(create_contact.id, group_get_random.id)
        old_contacts_in_group.append(create_contact)
    new_contacts_in_group = db.get_contacts_in_group(group_get_random)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)


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
    if len(db.get_group_list()) == 0:  # precondition rule for test
        app.group.create(group_value)
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact_value)
    group = db.get_group_list()
    contact = db.get_contact_list()
    group_get_random = random.choice(group)
    old_contacts_in_group = db.get_contacts_in_group(group_get_random)
    if len(old_contacts_in_group) != 0:
        contact_get_random = random.choice(old_contacts_in_group)
        app.contact.dell_contact_in_group(contact_get_random.id, group_get_random.id)
    else:
        contact_get_random = random.choice(contact)
        app.contact.add_contact_in_group(contact_get_random.id, group_get_random.id)
        old_contacts_in_group = db.get_contacts_in_group(group_get_random)
        app.contact.dell_contact_in_group(contact_get_random.id, group_get_random.id)
    old_contacts_in_group.remove(contact_get_random)
    new_contacts_in_group = db.get_contacts_in_group(group_get_random)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
