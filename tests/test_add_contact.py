from model.contact import Contact
import random
import string
import pytest


def random_string_for_group(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                     home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", byear="",
                     ayear="", adress2="", phone2="", notes="")] + \
            [Contact(
             firstname=random_string_for_group("firstname", 10),
             middlename=random_string_for_group("middlename", 10),
             lastname=random_string_for_group("lastname", 10),
             nickname=random_string_for_group("nickname", 10),
             title=random_string_for_group("title", 10),
             company=random_string_for_group("company", 10),
             address=random_string_for_group("address", 10),
             home=random_string_for_group("home", 10),
             mobile=random_string_for_group("mobile", 10),
             work=random_string_for_group("work", 10),
             fax=random_string_for_group("fax", 10),
             email=random_string_for_group("email", 10),
             email2=random_string_for_group("email2", 10),
             email3=random_string_for_group("email3", 10),
             homepage=random_string_for_group("homepage", 10),
             byear=random_string_for_group("byear", 10),
             ayear=random_string_for_group("ayear", 10),
             adress2=random_string_for_group("adress2", 10),
             phone2=random_string_for_group("phone2", 10),
             notes=random_string_for_group("notes", 10)) for i in range(5)]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_create_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
