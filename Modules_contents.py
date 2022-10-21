from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import threading

def module_contents(user_ID, module_ID):
    conn = sqlite3.connect("IP.db")
    cur = conn.cursor()

    content_name_list = []
    content_ID_list = []
    content_path_list = []

    user_type = cur.execute("SELECT user_type FROM USER WHERE user_ID=:user_ID",
                           {"user_ID": user_ID}).fetchone()[0]

    class_ID = cur.execute("SELECT class_ID FROM CLASS WHERE user_ID=:user_ID",
                           {"user_ID": user_ID}).fetchone()[0]

    content_name = cur.execute("SELECT content_name FROM CONTENT WHERE class_ID=:class_ID AND module_ID=:module_ID",
                            {"class_ID": class_ID, "module_ID": module_ID}).fetchall()

    content_ID = cur.execute("SELECT content_ID FROM CONTENT WHERE class_ID=:class_ID AND module_ID=:module_ID",
                               {"class_ID": class_ID, "module_ID": module_ID}).fetchall()

    content_path = cur.execute("SELECT file_path FROM CONTENT WHERE class_ID=:class_ID AND module_ID=:module_ID",
                               {"class_ID": class_ID, "module_ID": module_ID}).fetchall()

    for content in content_name:
        content_name_list.append(list(content)[0])

    for content in content_ID:
        content_ID_list.append(list(content)[0])

    for path in content_path:
        content_path_list.append(list(path)[0])

    CC = Tk()
    CC.title("Module contents")
    CC.geometry("700x700")
    CC.resizable(False, False)
    CC.config(bg="#1b1b1b")

    def open_content(index):
        from content_client import download_file
        download_file(content_path_list[index])
        print(f"Content Downloaded: {content_name_list[index]}")

    def prev(index):
        content_1_LF.config(text=content_name_list[index])
        course_content_1.config(command=lambda: open_content(index))
        pointer = len(content_name_list) - index
        if pointer % 3 == 1 and pointer < 3:
            content_2_LF = LabelFrame(CC, text="None", bg="#1b1b1b", fg="#F0E6FA")
            content_3_LF = LabelFrame(CC, text="None", bg="#1b1b1b", fg="#F0E6FA")
            course_content_2 = Button(content_2_LF, image=content_image,
                                      width=450, height=125, state=DISABLED)
            course_content_3 = Button(content_3_LF, image=content_image,
                                      width=450, height=125, state=DISABLED)
            content_2_LF.grid(row=1, column=1, pady=60, columnspan=10)
            content_3_LF.grid(row=2, column=1, columnspan=10)
            course_content_2.pack()
            course_content_3.pack()
        elif pointer % 3 == 2 and pointer < 3:
            content_2_LF = LabelFrame(CC, text=content_name_list[index+1], bg="#1b1b1b", fg="#F0E6FA")
            content_3_LF = LabelFrame(CC, text="None", bg="#1b1b1b", fg="#F0E6FA")

            course_content_2 = Button(content_2_LF, image=content_image,
                                      width=450, height=125, command=lambda: open_content(index + 1))
            course_content_3 = Button(content_3_LF, image=content_image,
                                      width=450, height=125, state=DISABLED)
            content_2_LF.grid(row=1, column=1, pady=60, columnspan=10)
            content_3_LF.grid(row=2, column=1, columnspan=10)
            course_content_2.pack()
            course_content_3.pack()
        else:
            content_2_LF = LabelFrame(CC, text=content_name_list[index+1], bg="#1b1b1b", fg="#F0E6FA")
            content_3_LF = LabelFrame(CC, text=content_name_list[index+2], bg="#1b1b1b", fg="#F0E6FA")
            course_content_2 = Button(content_2_LF, image=content_image,
                                      width=450, height=125, command=lambda: open_content(index + 1))
            course_content_3 = Button(content_3_LF, image=content_image,
                                      width=450, height=125, command=lambda: open_content(index + 2))
            content_2_LF.grid(row=1, column=1, pady=60, columnspan=10)
            content_3_LF.grid(row=2, column=1, columnspan=10)
            course_content_2.pack()
            course_content_3.pack()

        prev_btn = Button(CC, text="<<", command=lambda: prev(index - 3))
        next_btn = Button(CC, text=">>", command=lambda: next(index + 3))

        if index == 0:
            prev_btn = Button(CC, text="<<", state=DISABLED)

        prev_btn.grid(row=4, column=1)
        next_btn.grid(row=4, column=3)

    def next(index):
        content_1_LF.config(text=content_name_list[index])
        course_content_1.config(command=lambda: open_content(index))
        pointer = len(content_name_list) - index
        if pointer % 3 == 1 and pointer < 3:
            content_2_LF = LabelFrame(CC, text="None", bg="#1b1b1b", fg="#F0E6FA")
            content_3_LF = LabelFrame(CC, text="None", bg="#1b1b1b", fg="#F0E6FA")
            course_content_2 = Button(content_2_LF, image=content_image,
                                      width=450, height=125, state=DISABLED)
            course_content_3 = Button(content_3_LF, image=content_image,
                                      width=450, height=125, state=DISABLED)
            content_2_LF.grid(row=1, column=1, pady=60, columnspan=10)
            content_3_LF.grid(row=2, column=1, columnspan=10)
            course_content_2.pack()
            course_content_3.pack()
        elif pointer % 3 == 2 and pointer < 3:
            content_2_LF = LabelFrame(CC, text=content_name_list[index + 1], bg="#1b1b1b", fg="#F0E6FA")
            content_3_LF = LabelFrame(CC, text="None", bg="#1b1b1b", fg="#F0E6FA")

            course_content_2 = Button(content_2_LF, image=content_image,
                                      width=450, height=125, command=lambda: open_content(index + 1))
            course_content_3 = Button(content_3_LF, image=content_image,
                                      width=450, height=125, state=DISABLED)
            content_2_LF.grid(row=1, column=1, pady=60, columnspan=10)
            content_3_LF.grid(row=2, column=1, columnspan=10)
            course_content_2.pack()
            course_content_3.pack()
        else:
            content_2_LF = LabelFrame(CC, text=content_name_list[index + 1], bg="#1b1b1b", fg="#F0E6FA")
            content_3_LF = LabelFrame(CC, text=content_name_list[index + 2], bg="#1b1b1b", fg="#F0E6FA")
            course_content_2 = Button(content_2_LF, image=content_image,
                                      width=450, height=125, command=lambda: open_content(index + 1))
            course_content_3 = Button(content_3_LF, image=content_image,
                                      width=450, height=125, command=lambda: open_content(index + 2))
            content_2_LF.grid(row=1, column=1, pady=60, columnspan=10)
            content_3_LF.grid(row=2, column=1, columnspan=10)
            course_content_2.pack()
            course_content_3.pack()

        prev_btn = Button(CC, text="<<", command=lambda: prev(index - 3))
        next_btn = Button(CC, text=">>", command=lambda: next(index + 3))

        if index >= len(content_name_list) - 3:
            next_btn = Button(CC, text=">>", state=DISABLED)

        prev_btn.grid(row=4, column=1)
        next_btn.grid(row=4, column=3)

    def edit():
        from Edit_module import edit_cours_win
        edit_cours_win(user_ID, module_ID)

    def back():
        CC.destroy()
        conn.close()
        from Modules import courses_window
        courses_window(user_ID)

    #   Images
    rec_image = ImageTk.PhotoImage(Image.open(f"Images/video_recoding_1.png"))
    content_image = ImageTk.PhotoImage(Image.open(f"Images/content_1.png"))

    #   LabelFrame
    session_LF = LabelFrame(CC, text="None", bg="#1b1b1b", fg="#F0E6FA")
    content_1_LF = LabelFrame(CC, text=content_name_list[0], bg="#1b1b1b", fg="#F0E6FA")
    content_2_LF = LabelFrame(CC, text=content_name_list[1], bg="#1b1b1b", fg="#F0E6FA")
    content_3_LF = LabelFrame(CC, text=content_name_list[2], bg="#1b1b1b", fg="#F0E6FA")

    #   Gap
    gap = Label(CC, bg="#1b1b1b")

    #   Button
    join_btn = Button(session_LF, image=rec_image, width=175, height=125, state=DISABLED)

    course_content_1 = Button(content_1_LF, image=content_image,
                              width=450, height=125, command=lambda: open_content(0))
    course_content_2 = Button(content_2_LF, image=content_image,
                              width=450, height=125, command=lambda: open_content(1))
    course_content_3 = Button(content_3_LF, image=content_image,
                              width=450, height=125, command=lambda: open_content(2))

    prev_btn = Button(CC, text="<<", state=DISABLED)
    edit_course = Button(CC, text="Edit Module", command=edit)
    next_btn = Button(CC, text=">>", command=lambda: next(3))
    if len(content_name_list) < 4:
        next_btn = Button(CC, text=">>", state=DISABLED)

    back_btn = Button(CC, text="Back", width=6, height=1, command=back)

    #   Grid
    session_LF.grid(row=0, column=0, padx=20)
    content_1_LF.grid(row=0, column=1, columnspan=10)
    content_2_LF.grid(row=1, column=1, pady=60, columnspan=10)
    content_3_LF.grid(row=2, column=1, columnspan=10)
    prev_btn.grid(row=4, column=1)

    if user_type == "Teacher":
        edit_course.grid(row=4, column=2, padx=160)
    if user_type == "Teacher":
        next_btn.grid(row=4, column=3)
    else:
        gap.grid(row=4, column=2, padx=190)
        next_btn.grid(row=4, column=3)

    back_btn.grid(row=4, column=0, sticky=W, pady=50, padx=30)

    #   Pack
    join_btn.pack()

    course_content_1.pack()
    course_content_2.pack()
    course_content_3.pack()

    mainloop()