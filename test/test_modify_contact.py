# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_first_contact_all(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(nickname="Knyazeva"))
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    contact_mod = Contact(firstname="Modify1", middlename="Modify2", lastname="Modify3", nickname="Modify", photo="C:\\Users\Ann\Downloads\cat1.jpg", title="TrainingModify",
                               company="Software-Testing-Modify", address="Barnaul-Modify", home_phone="654321", mobile_phone="1111111119", work_phone="321", fax="ytrewq", email_1="Modify1@Modify.ru",
                               email_2="Modify2@Modify.ru", email_3="Modify3@Modify.ru", homepage="Modify.ru", bday="10", byear="1991", aday="12", ayear="1992", bmonth="January", amonth="March", id=contact.id)
    app.contact.modify_contact_by_id(contact.id, contact_mod)
    new_contact = db.get_contact_list()
    assert len(old_contact) == len(new_contact)
    index = old_contact.index(contact)
    old_contact[index] = contact_mod
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
