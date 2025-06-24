# -*- coding: utf-8 -*-
from application import Application
from contact import Contact
import unittest


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="Anna1", middlename="Anna2", lastname="Anna3", nickname="Knyazeva", photo="C:\\Users\Ann\Downloads\cat.jpg", title="Training",
                            company="Software-Testing", address="Barnaul", home_phone="123456", mobile_phone="9111111111", work_phone="123", fax="qwerty", email_1="test1@test.ru",
                            email_2="test2@test.ru", email_3="test3@test.ru", homepage="test.ru", bday="1", byear="1911", aday="2", ayear="1922", bmonth="March", amonth="January"))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
