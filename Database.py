import sqlite3
from init import *

conn = sqlite3.connect('IP.db')
cur = conn.cursor()


def insert_user(user):
    with conn:
        cur.execute("INSERT INTO USER VALUES (:user_ID, :user_type, :fullname, :username, :password)",
                    {'user_ID': user.user_ID, 'user_type': user.user_type,
                     "fullname": user.fullname,
                     'username': user.username, 'password': user.password})


def insert_class(Class):
    with conn:
        cur.execute("INSERT INTO CLASS VALUES (:class_ID, :user_ID)",
                    {"class_ID": Class.class_ID, "user_ID": Class.user_ID})


def insert_module(module):
    with conn:
        cur.execute("INSERT INTO MODULE VALUES (:module_ID, :module_name, :class_ID, :file_path)",
                    {"module_ID": module.module_ID, "module_name": module.module_name,
                     "class_ID": module.class_ID, "file_path": module.file_path})


cur.execute('''
            CREATE TABLE USER
            (
                user_ID integer,
                user_type text,
                fullname text,
                username text,
                password text
            )
            '''
            )

cur.execute('''
            CREATE TABLE CLASS
            (
                class_ID integer,
                user_ID integer
            )
            '''
            )

cur.execute('''
            CREATE TABLE MODULE
            (
                module_ID integer,
                module_name text,
                class_ID integer,
                file_path text
            )
            '''
            )

cur.execute('''
            CREATE TABLE CONTENT
            (
                content_ID integer,
                content_name text,
                class_ID text,
                file_path text,
                module_ID integer
            )
            '''
            )

admin_user = user(1000, "Admin", "Rafael Almonte", "rafael.al_1000", "orange103")
stud_user_1 = user(1001, "Student", "Student_1", "someone_1.1001", "orange103")
stud_user_2 = user(1002, "Student", "Student_2", "someone_1.1002", "orange103")
stud_user_3 = user(1003, "Student", "Student_3", "someone_1.1003", "orange103")  # ---> class 1
stud_user_4 = user(1004, "Student", "Student_4", "someone_1.1004", "orange103")
stud_user_5 = user(1005, "Student", "Student_5", "someone_1.1005", "orange103")
stud_user_6 = user(1006, "Student", "Student_6", "someone_1.1006", "orange103")  # ---> class 2
stud_user_7 = user(1007, "Student", "Student_7", "someone_1.1007", "orange103")
stud_user_8 = user(1008, "Student", "Student_8", "someone_1.1008", "orange103")
stud_user_9 = user(1009, "Student", "Student_9", "someone_1.1009", "orange103")  # ---> class 3
lect_user_1 = user(5001, "Teacher", "Lecturer_1", "someone_1.5001", "orange103")  # ---> class 1
lect_user_2 = user(5002, "Teacher", "Lecturer_2", "someone_1.5002", "orange103")  # ---> class 2
lect_user_3 = user(5003, "Teacher", "Lecturer_3", "someone_1.5003", "orange103")  # ---> class 3

insert_user(admin_user)
insert_user(stud_user_1)
insert_user(stud_user_2)
insert_user(stud_user_3)
insert_user(stud_user_4)
insert_user(stud_user_5)
insert_user(stud_user_6)
insert_user(stud_user_7)
insert_user(stud_user_8)
insert_user(stud_user_9)
insert_user(lect_user_1)
insert_user(lect_user_2)
insert_user(lect_user_3)

module_1_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 1"
module_2_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 2"
module_3_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 3"
module_4_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 4"
module_5_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 5"
module_6_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 6"
module_7_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 7"
module_8_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 8"
module_9_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 9"

module_1_class_1 = module(10001, "Module 1", 1, module_1_path)
module_2_class_1 = module(10002, "Module 2", 1, module_2_path)
module_3_class_1 = module(10003, "Module 3", 1, module_3_path)

module_1_class_2 = module(10001, "Module 1", 2, module_1_path)
module_2_class_2 = module(10002, "Module 2", 2, module_2_path)
module_3_class_2 = module(10003, "Module 3", 2, module_3_path)
module_4_class_2 = module(10004, "Module 4", 2, module_4_path)
module_5_class_2 = module(10005, "Module 5", 2, module_5_path)
module_6_class_2 = module(10006, "Module 6", 2, module_6_path)
module_7_class_2 = module(10007, "Module 7", 2, module_7_path)
module_8_class_2 = module(10008, "Module 8", 2, module_8_path)
module_9_class_2 = module(10009, "Module 9", 2, module_9_path)

module_3_class_3 = module(10003, "Module 3", 3, module_3_path)
module_6_class_3 = module(10006, "Module 6", 3, module_6_path)
module_9_class_3 = module(10009, "Module 9", 3, module_9_path)

insert_module(module_1_class_1)
insert_module(module_2_class_1)
insert_module(module_3_class_1)

insert_module(module_1_class_2)
insert_module(module_2_class_2)
insert_module(module_3_class_2)
insert_module(module_4_class_2)
insert_module(module_5_class_2)
insert_module(module_6_class_2)
insert_module(module_7_class_2)
insert_module(module_8_class_2)
insert_module(module_9_class_2)

insert_module(module_3_class_3)
insert_module(module_6_class_3)
insert_module(module_9_class_3)

class_1_lect_1 = Class(1, 5001)
class_1_stud_1 = Class(1, 1001)
class_1_stud_2 = Class(1, 1002)
class_1_stud_3 = Class(1, 1003)

class_2_lect_2 = Class(2, 5002)
class_2_stud_1 = Class(2, 1004)
class_2_stud_2 = Class(2, 1005)
class_2_stud_3 = Class(2, 1006)

class_3_lect_3 = Class(3, 5003)
class_3_stud_1 = Class(3, 1007)
class_3_stud_2 = Class(3, 1008)
class_3_stud_3 = Class(3, 1009)


insert_class(class_1_lect_1)
insert_class(class_1_stud_1)
insert_class(class_1_stud_2)
insert_class(class_1_stud_3)

insert_class(class_2_lect_2)
insert_class(class_2_stud_1)
insert_class(class_2_stud_2)
insert_class(class_2_stud_3)

insert_class(class_3_lect_3)
insert_class(class_3_stud_1)
insert_class(class_3_stud_2)
insert_class(class_3_stud_3)

conn.close()
