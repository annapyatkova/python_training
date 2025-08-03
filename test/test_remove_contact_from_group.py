from fixture.db import DbFixture
from model.group import Group
from model.contact import Contact
import random

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_remove_contact_from_group(app, db, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="newtest", header="newtest", footer="newtest"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="newModify1", middlename="newModify2", lastname="newModify3", nickname="newModify", photo="C:\\Users\Ann\Downloads\cat1.jpg", title="TrainingModify",
                               company="Software-Testing-Modify", address="Barnaul-Modify", home_phone="654321", mobile_phone="1111111119", work_phone="321", fax="ytrewq", email_1="Modify1@Modify.ru",
                               email_2="Modify2@Modify.ru", email_3="Modify3@Modify.ru", homepage="Modify.ru", bday="10", byear="1991", aday="12", ayear="1992", bmonth="January", amonth="March"))
    if len(orm.get_contacts_with_group()) == 0:
        group_list = db.get_group_list()
        group = random.choice(group_list)
        contact_list = db.get_contact_list()
        contact = random.choice(contact_list)
        app.contact.add_to_group(contact.id, group.id)
    contacts_with_group = orm.get_contacts_with_group()
    contact = random.choice(contacts_with_group)
    groups_contact = orm.get_groups_contact(contact)
    group = random.choice(groups_contact)
    assert group in groups_contact
    app.contact.remove_from_group(contact.id, group.id)
    groups_contact = orm.get_groups_contact(contact)
    assert group not in groups_contact