from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact,
                       table="address_in_groups",
                       column="id",
                       reverse="groups",
                       lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        middlename = Optional(str, column='middlename')
        nickname = Optional(str, column='nickname')
        title = Optional(str, column='title')
        company = Optional(str, column='company')
        address = Optional(str, column='address')
        home = Optional(str, column='home')
        mobile = Optional(str, column='mobile')
        work = Optional(str, column='work')
        fax = Optional(str, column='fax')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        homepage = Optional(str, column='homepage')
        byear = Optional(str, column='byear')
        ayear = Optional(str, column='ayear')
        adress2 = Optional(str, column='address2')
        phone2 = Optional(str, column='phone2')
        notes = Optional(str, column='notes')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup,
                     table="address_in_groups",
                     column="group_id",
                     reverse="contacts",
                     lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql',
                     host=host,
                     database=name,
                     user=user,
                     password=password,)
        self.db.generate_mapping()
        sql_debug(True)

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id),
                           firstname=contact.firstname,
                           lastname=contact.lastname,
                           middlename=contact.middlename,
                           nickname=contact.nickname,
                           title=contact.title,
                           company=contact.company,
                           address=contact.address,
                           home=contact.home,
                           mobile=contact.mobile,
                           work=contact.work,
                           fax=contact.fax,
                           email=contact.email,
                           email2=contact.email2,
                           email3=contact.email3,
                           homepage=contact.homepage,
                           byear=contact.byear,
                           ayear=contact.ayear,
                           adress2=contact.adress2,
                           phone2=contact.adress2,
                           notes=contact.notes)
        return list(map(convert, contacts))

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id),
                         name=group.name,
                         header=group.header,
                         footer=group.footer)
        return list(map(convert, groups))

