# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="Anna1", middlename="Anna2", lastname="Anna3", nickname="Knyazeva", photo="C:\\Users\Ann\Downloads\cat.jpg", title="Training",
                               company="Software-Testing", address="Barnaul", home_phone="123456", mobile_phone="9111111111", work_phone="123", fax="qwerty", email_1="test1@test.ru",
                               email_2="test2@test.ru", email_3="test3@test.ru", homepage="test.ru", bday="1", byear="1911", aday="2", ayear="1922", bmonth="March", amonth="January")
    app.contact.create(contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)