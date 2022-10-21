from tkinter import *
from PIL import ImageTk, Image
import sqlite3


def courses_window(ID):
    conn = sqlite3.connect("IP.db")
    cur = conn.cursor()

    course_file_path_list = []
    course_name_list = []
    course_ID_list = []

    user_type = cur.execute("SELECT user_type FROM USER WHERE user_ID=:user_ID",
                            {"user_ID": ID}).fetchone()[0]

    class_ID = cur.execute("SELECT class_ID FROM CLASS WHERE user_ID=:user_ID",
                            {"user_ID": ID}).fetchone()[0]

    course_ID = cur.execute("SELECT module_ID FROM MODULE WHERE class_ID=:class_ID",
                            {"class_ID": class_ID}).fetchall()

    for course in course_ID:
        course_ID_list.append(list(course)[0])

    if user_type == "Teacher":
        lect_class = cur.execute("SELECT class_ID FROM CLASS WHERE user_ID=:user_ID",
                                  {"user_ID": ID}).fetchone()[0]
        lect_course_path = cur.execute("SELECT file_path FROM MODULE WHERE class_ID=:class_ID",
                                  {"class_ID": lect_class}).fetchall()
        course_name = cur.execute("SELECT module_name FROM MODULE WHERE class_ID=:class_ID",
                                  {"class_ID": lect_class}).fetchall()

        for path in lect_course_path:
            course_file_path_list.append(list(path)[0])

        for name in course_name:
            course_name_list.append(list(name)[0])
    else:
        stud_class = cur.execute("SELECT class_ID FROM CLASS WHERE user_ID=:user_ID",
                                 {"user_ID": ID}).fetchone()[0]
        stud_course_path = cur.execute("SELECT file_path FROM MODULE WHERE class_ID=:class_ID",
                                       {"class_ID": stud_class}).fetchall()
        course_name = cur.execute("SELECT module_name FROM MODULE WHERE class_ID=:class_ID",
                                  {"class_ID": stud_class}).fetchall()

        for path in stud_course_path:
            course_file_path_list.append(list(path)[0])

        for name in course_name:
            course_name_list.append(list(name)[0])

    CW = Tk()
    CW.title("Modules")
    CW.geometry("700x500")
    CW.resizable(False, False)
    CW.config(bg="#1b1b1b")

    def goto_course_contents(index):
        CW.destroy()
        conn.close()
        from Modules_contents import module_contents
        module_contents(ID, course_ID_list[index])

    def prev(index):
        course_pos_1.config(text=course_name_list[index])
        course_pos_1_btn.config(command=lambda: goto_course_contents(index))
        pointer = len(course_name_list) - index
        if pointer % 3 == 1 and pointer < 3:
            course_pos_2 = LabelFrame(CW, text="None", bg="#1b1b1b", fg="#F0E6FA")
            course_pos_3 = LabelFrame(CW, text="None", bg="#1b1b1b", fg="#F0E6FA")
            course_pos_2_btn = Button(course_pos_2, image=course_image,
                                      width=175, height=125, state=DISABLED)
            course_pos_3_btn = Button(course_pos_3, image=course_image,
                                      width=175, height=125, state=DISABLED)
            course_pos_2.grid(row=1, column=1, padx=20)
            course_pos_3.grid(row=1, column=2, padx=20)
            course_pos_2_btn.pack()
            course_pos_3_btn.pack()
        elif pointer % 3 == 2 and pointer < 3:
            course_pos_2 = LabelFrame(CW, text=course_name_list[index + 1], bg="#1b1b1b", fg="#F0E6FA")
            course_pos_3 = LabelFrame(CW, text="None", bg="#1b1b1b", fg="#F0E6FA")
            course_pos_2_btn = Button(course_pos_2, image=course_image,
                                      width=175, height=125, command=lambda: goto_course_contents(index + 1))
            course_pos_3_btn = Button(course_pos_3, image=course_image,
                                      width=175, height=125, state=DISABLED)
            course_pos_2.grid(row=1, column=1, padx=20)
            course_pos_3.grid(row=1, column=2, padx=20)
            course_pos_2_btn.pack()
            course_pos_3_btn.pack()
        else:
            course_pos_2 = LabelFrame(CW, text=course_name_list[index + 1], bg="#1b1b1b", fg="#F0E6FA")
            course_pos_3 = LabelFrame(CW, text=course_name_list[index + 2], bg="#1b1b1b", fg="#F0E6FA")
            course_pos_2_btn = Button(course_pos_2, image=course_image,
                                      width=175, height=125, command=lambda: goto_course_contents(index + 1))
            course_pos_3_btn = Button(course_pos_3, image=course_image,
                                      width=175, height=125, command=lambda: goto_course_contents(index + 2))
            course_pos_2.grid(row=1, column=1, padx=20)
            course_pos_3.grid(row=1, column=2, padx=20)
            course_pos_2_btn.pack()
            course_pos_3_btn.pack()

        prev_btn = Button(CW, text="<<", command=lambda: prev(index - 3))
        next_btn = Button(CW, text=">>", command=lambda: next(index + 3))

        if index == 0:
            prev_btn = Button(CW, text="<<", state=DISABLED)

        prev_btn.grid(row=3, column=0)
        next_btn.grid(row=3, column=2)

    def next(index):
        course_pos_1.config(text=course_name_list[index])
        course_pos_1_btn.config(command=lambda: goto_course_contents(index))
        pointer = len(course_name_list) - index
        if pointer % 3 == 1 and pointer < 3:
            course_pos_2 = LabelFrame(CW, text="None", bg="#1b1b1b", fg="#F0E6FA")
            course_pos_3 = LabelFrame(CW, text="None", bg="#1b1b1b", fg="#F0E6FA")
            course_pos_2_btn = Button(course_pos_2, image=course_image,
                                      width=175, height=125, state=DISABLED)
            course_pos_3_btn = Button(course_pos_3, image=course_image,
                                      width=175, height=125, state=DISABLED)
            course_pos_2.grid(row=1, column=1, padx=20)
            course_pos_3.grid(row=1, column=2, padx=20)
            course_pos_2_btn.pack()
            course_pos_3_btn.pack()
        elif pointer % 3 == 2 and pointer < 3:
            course_pos_2 = LabelFrame(CW, text=course_name_list[index + 1], bg="#1b1b1b", fg="#F0E6FA")
            course_pos_3 = LabelFrame(CW, text="None", bg="#1b1b1b", fg="#F0E6FA")
            course_pos_2_btn = Button(course_pos_2, image=course_image,
                                      width=175, height=125, command=lambda: goto_course_contents(index + 1))
            course_pos_3_btn = Button(course_pos_3, image=course_image,
                                      width=175, height=125, state=DISABLED)
            course_pos_2.grid(row=1, column=1, padx=20)
            course_pos_3.grid(row=1, column=2, padx=20)
            course_pos_2_btn.pack()
            course_pos_3_btn.pack()
        else:
            course_pos_2 = LabelFrame(CW, text=course_name_list[index + 1], bg="#1b1b1b", fg="#F0E6FA")
            course_pos_3 = LabelFrame(CW, text=course_name_list[index + 2], bg="#1b1b1b", fg="#F0E6FA")
            course_pos_2_btn = Button(course_pos_2, image=course_image,
                                      width=175, height=125, command=lambda: goto_course_contents(index + 1))
            course_pos_3_btn = Button(course_pos_3, image=course_image,
                                      width=175, height=125, command=lambda: goto_course_contents(index + 2))
            course_pos_2.grid(row=1, column=1, padx=20)
            course_pos_3.grid(row=1, column=2, padx=20)
            course_pos_2_btn.pack()
            course_pos_3_btn.pack()

        prev_btn = Button(CW, text="<<", command=lambda: prev(index-3))
        next_btn = Button(CW, text=">>", command=lambda: next(index+3))

        if index >= len(course_name_list) - 3:
            next_btn = Button(CW, text=">>", state=DISABLED)

        prev_btn.grid(row=3, column=0)
        next_btn.grid(row=3, column=2)

    def back():
        if user_type == "Teacher":
            CW.destroy()
            conn.close()
            from Lect_window import teacher_window
            teacher_window(ID)
        else:
            CW.destroy()
            conn.close()
            from Stud_window import student_win
            student_win(ID)

    #   Image
    course_image = ImageTk.PhotoImage(Image.open(f"Images/courses_1.jpg"))

    #   Gap
    gap0 = Label(CW, bg="#1b1b1b")
    gap1 = Label(CW, bg="#1b1b1b")
    gap2 = Label(CW, bg="#1b1b1b")

    #   LabelFrame
    course_pos_1 = LabelFrame(CW, text=course_name_list[0], bg="#1b1b1b", fg="#F0E6FA")
    course_pos_2 = LabelFrame(CW, text=course_name_list[1], bg="#1b1b1b", fg="#F0E6FA")
    course_pos_3 = LabelFrame(CW, text=course_name_list[2], bg="#1b1b1b", fg="#F0E6FA")

    #   Button
    course_pos_1_btn = Button(course_pos_1, image=course_image,
                              width=175, height=125, command=lambda: goto_course_contents(0))
    course_pos_2_btn = Button(course_pos_2, image=course_image,
                              width=175, height=125, command=lambda: goto_course_contents(1))
    course_pos_3_btn = Button(course_pos_3, image=course_image,
                              width=175, height=125, command=lambda: goto_course_contents(2))

    prev_btn = Button(CW, text="<<", state=DISABLED)
    next_btn = Button(CW, text=">>", state=DISABLED)
    if len(course_ID_list) > 3:
        next_btn = Button(CW, text=">>", command=lambda: next(3))

    back_btn = Button(CW, text="Back", command=back)

    #   Grid
    gap0.grid(row=0, column=0, pady=30)
    course_pos_1.grid(row=1, column=0, padx=20)
    if len(course_ID_list) > 1:
        course_pos_2.grid(row=1, column=1, padx=20)
    if len(course_ID_list) > 2:
        course_pos_3.grid(row=1, column=2, padx=20)
    gap1.grid(row=2, column=0, pady=30)
    prev_btn.grid(row=3, column=0)
    next_btn.grid(row=3, column=2)
    gap2.grid(row=4, column=0, pady=30)
    back_btn.grid(row=5, column=0, sticky=W, padx=20)

    #   Pack
    course_pos_1_btn.pack()
    course_pos_2_btn.pack()
    course_pos_3_btn.pack()

    CW.mainloop()