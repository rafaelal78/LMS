import sqlite3
from init import content

conn = sqlite3.connect('IP.db')
cur = conn.cursor()

def insert_content(content):
    with conn:
        cur.execute("INSERT INTO CONTENT VALUES (:content_ID, :content_name, :class_ID,"
                    " :file_path, :module_ID)",
                    {"content_ID": content.content_ID, "content_name": content.content_name,
                     "class_ID": content.class_ID, "file_path": content.absolute_path,
                     "module_ID": content.module_ID})

c1c1_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 1\academical1_content_1.txt"
c1c2_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 1\academical1_content_2.txt"
c1c3_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 1\academical1_content_3.txt"

c2c1_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 2\academical2_content_1.txt"
c2c2_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 2\academical2_content_2.txt"
c2c3_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 2\academical2_content_3.txt"

c3c1_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 3\academical3_content_1.txt"
c3c2_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 3\academical3_content_2.txt"
c3c3_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 3\academical3_content_3.txt"

c4c1_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 4\academical4_content_1.txt"
c4c2_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 4\academical4_content_2.txt"
c4c3_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 4\academical4_content_3.txt"

c5c1_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 5\academical5_content_1.txt"
c5c2_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 5\academical5_content_2.txt"
c5c3_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 5\academical5_content_3.txt"

c6c1_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 6\academical6_content_1.txt"
c6c2_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 6\academical6_content_2.txt"
c6c3_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 6\academical6_content_3.txt"

c7c1_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 7\academical7_content_1.txt"
c7c2_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 7\academical7_content_2.txt"
c7c3_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 7\academical7_content_3.txt"

c8c1_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 8\academical8_content_1.txt"
c8c2_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 8\academical8_content_2.txt"
c8c3_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 8\academical8_content_3.txt"

c9c1_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 9\academical9_content_1.txt"
c9c2_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 9\academical9_content_2.txt"
c9c3_path = r"C:\Users\lenovo\PycharmProjects\LMS\modules\Module 9\academical9_content_3.txt"

course_1_content_1_class_1 = content(10011, "academical1_content_1", 1, c1c1_path, 10001)
course_1_content_2_class_1 = content(10021, "academical1_content_2", 1, c1c2_path, 10001)
course_1_content_3_class_1 = content(10031, "academical1_content_3", 1, c1c3_path, 10001)
course_2_content_1_class_1 = content(10012, "academical2_content_1", 1, c2c1_path, 10002)
course_2_content_2_class_1 = content(10022, "academical2_content_2", 1, c2c2_path, 10002)
course_2_content_3_class_1 = content(10032, "academical2_content_3", 1, c2c3_path, 10002)
course_3_content_1_class_1 = content(10013, "academical3_content_1", 1, c3c1_path, 10003)
course_3_content_2_class_1 = content(10023, "academical3_content_2", 1, c3c2_path, 10003)
course_3_content_3_class_1 = content(10033, "academical3_content_3", 1, c3c3_path, 10003)

course_1_content_1_class_2 = content(10011, "academical1_content_1", 2, c1c1_path, 10001)
course_1_content_2_class_2 = content(10021, "academical1_content_2", 2, c1c2_path, 10001)
course_1_content_3_class_2 = content(10031, "academical1_content_3", 2, c1c3_path, 10001)
course_2_content_1_class_2 = content(10012, "academical2_content_1", 2, c2c1_path, 10002)
course_2_content_2_class_2 = content(10022, "academical2_content_2", 2, c2c2_path, 10002)
course_2_content_3_class_2 = content(10032, "academical2_content_3", 2, c2c3_path, 10002)
course_3_content_1_class_2 = content(10013, "academical3_content_1", 2, c3c1_path, 10003)
course_3_content_2_class_2 = content(10023, "academical3_content_2", 2, c3c2_path, 10003)
course_3_content_3_class_2 = content(10033, "academical3_content_3", 2, c3c3_path, 10003)
course_4_content_1_class_2 = content(10014, "academical4_content_1", 2, c4c1_path, 10004)
course_4_content_2_class_2 = content(10024, "academical4_content_2", 2, c4c2_path, 10004)
course_4_content_3_class_2 = content(10034, "academical4_content_3", 2, c4c3_path, 10004)
course_5_content_1_class_2 = content(10015, "academical5_content_1", 2, c5c1_path, 10005)
course_5_content_2_class_2 = content(10025, "academical5_content_2", 2, c5c2_path, 10005)
course_5_content_3_class_2 = content(10035, "academical5_content_3", 2, c5c3_path, 10005)
course_6_content_1_class_2 = content(10016, "academical6_content_1", 2, c6c1_path, 10006)
course_6_content_2_class_2 = content(10026, "academical6_content_2", 2, c6c2_path, 10006)
course_6_content_3_class_2 = content(10036, "academical6_content_3", 2, c6c3_path, 10006)
course_7_content_1_class_2 = content(10017, "academical7_content_1", 2, c7c1_path, 10007)
course_7_content_2_class_2 = content(10027, "academical7_content_2", 2, c7c2_path, 10007)
course_7_content_3_class_2 = content(10037, "academical7_content_3", 2, c7c3_path, 10007)
course_8_content_1_class_2 = content(10018, "academical8_content_1", 2, c8c1_path, 10008)
course_8_content_2_class_2 = content(10028, "academical8_content_2", 2, c8c2_path, 10008)
course_8_content_3_class_2 = content(10038, "academical8_content_3", 2, c8c3_path, 10008)
course_9_content_1_class_2 = content(10019, "academical9_content_1", 2, c9c1_path, 10009)
course_9_content_2_class_2 = content(10029, "academical9_content_2", 2, c9c2_path, 10009)
course_9_content_3_class_2 = content(10039, "academical9_content_3", 2, c9c3_path, 10009)

course_3_content_1_class_3 = content(10013, "academical3_content_1", 3, c3c1_path, 10003)
course_3_content_2_class_3 = content(10023, "academical3_content_2", 3, c3c2_path, 10003)
course_3_content_3_class_3 = content(10033, "academical3_content_3", 3, c3c3_path, 10003)
course_6_content_1_class_3 = content(10016, "academical6_content_1", 3, c6c1_path, 10006)
course_6_content_2_class_3 = content(10026, "academical6_content_2", 3, c6c2_path, 10006)
course_6_content_3_class_3 = content(10036, "academical6_content_3", 3, c6c3_path, 10006)
course_9_content_1_class_3 = content(10019, "academical9_content_1", 3, c9c1_path, 10009)
course_9_content_2_class_3 = content(10029, "academical9_content_2", 3, c9c2_path, 10009)
course_9_content_3_class_3 = content(10039, "academical9_content_3", 3, c9c3_path, 10009)

insert_content(course_1_content_1_class_1)
insert_content(course_1_content_2_class_1)
insert_content(course_1_content_3_class_1)
insert_content(course_2_content_1_class_1)
insert_content(course_2_content_2_class_1)
insert_content(course_2_content_3_class_1)
insert_content(course_3_content_1_class_1)
insert_content(course_3_content_2_class_1)
insert_content(course_3_content_3_class_1)

insert_content(course_1_content_1_class_2)
insert_content(course_1_content_2_class_2)
insert_content(course_1_content_3_class_2)
insert_content(course_2_content_1_class_2)
insert_content(course_2_content_2_class_2)
insert_content(course_2_content_3_class_2)
insert_content(course_3_content_1_class_2)
insert_content(course_3_content_2_class_2)
insert_content(course_3_content_3_class_2)
insert_content(course_4_content_1_class_2)
insert_content(course_4_content_2_class_2)
insert_content(course_4_content_3_class_2)
insert_content(course_5_content_1_class_2)
insert_content(course_5_content_2_class_2)
insert_content(course_5_content_3_class_2)
insert_content(course_6_content_1_class_2)
insert_content(course_6_content_2_class_2)
insert_content(course_6_content_3_class_2)
insert_content(course_7_content_1_class_2)
insert_content(course_7_content_2_class_2)
insert_content(course_7_content_3_class_2)
insert_content(course_8_content_1_class_2)
insert_content(course_8_content_2_class_2)
insert_content(course_8_content_3_class_2)
insert_content(course_9_content_1_class_2)
insert_content(course_9_content_2_class_2)
insert_content(course_9_content_3_class_2)

insert_content(course_3_content_1_class_3)
insert_content(course_3_content_2_class_3)
insert_content(course_3_content_3_class_3)
insert_content(course_6_content_1_class_3)
insert_content(course_6_content_2_class_3)
insert_content(course_6_content_3_class_3)
insert_content(course_9_content_1_class_3)
insert_content(course_9_content_2_class_3)
insert_content(course_9_content_3_class_3)

conn.close()