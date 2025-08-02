import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3 from addressbook where deprecated is NULL")
            for row in cursor:
                (id, firstname, lastname, address, home_phone, mobile_phone, work_phone, email_1, email_2, email_3) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, home_phone = home_phone,
                       mobile_phone = mobile_phone, work_phone = work_phone,  email_1=email_1,
                       email_2=email_2, email_3=email_3))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()