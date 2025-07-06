# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact_all(app):
    app.contact.modify_first_contact(Contact(firstname="Modify1", middlename="Modify2", lastname="Modify3", nickname="Modify", photo="C:\\Users\Ann\Downloads\cat1.jpg", title="TrainingModify",
                               company="Software-Testing-Modify", address="Barnaul-Modify", home_phone="654321", mobile_phone="1111111119", work_phone="321", fax="ytrewq", email_1="Modify1@Modify.ru",
                               email_2="Modify2@Modify.ru", email_3="Modify3@Modify.ru", homepage="Modify.ru", bday="10", byear="1991", aday="12", ayear="1992", bmonth="January", amonth="March"))