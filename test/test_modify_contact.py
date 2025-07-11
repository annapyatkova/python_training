# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_first_contact_all(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(nickname="Knyazeva"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact(firstname="Modify1", middlename="Modify2", lastname="Modify3", nickname="Modify", photo="C:\\Users\Ann\Downloads\cat1.jpg", title="TrainingModify",
                               company="Software-Testing-Modify", address="Barnaul-Modify", home_phone="654321", mobile_phone="1111111119", work_phone="321", fax="ytrewq", email_1="Modify1@Modify.ru",
                               email_2="Modify2@Modify.ru", email_3="Modify3@Modify.ru", homepage="Modify.ru", bday="10", byear="1991", aday="12", ayear="1992", bmonth="January", amonth="March")
    contact.id = old_contact[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)