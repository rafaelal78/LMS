import random
from tkinter import *
from tkinter import messagebox, filedialog
import sqlite3
import os
import re

def edit_cours_win(user_ID, module_ID):
    # 10039
    conn = sqlite3.connect("IP.db")
    cur = conn.cursor()

    # content_name = cur.execute("SELECT content_name FROM CONTENT WHERE content_ID=:content_ID",
    #                        {"content_ID": content_ID}).fetchone()[0]

    content_ID_list = []
    content_name_list = []

    module_name = cur.execute("SELECT module_name FROM MODULE WHERE module_ID=:module_ID",
                              {"module_ID": module_ID}).fetchone()[0]
    module_path = cur.execute("SELECT file_path FROM MODULE WHERE module_ID=:module_ID",
                              {"module_ID": module_ID}).fetchone()[0]

    class_ID = cur.execute("SELECT class_ID FROM CLASS WHERE user_ID=:user_ID",
                           {"user_ID": user_ID}).fetchone()[0]

    content_ID = cur.execute("SELECT content_ID FROM CONTENT WHERE class_ID=:class_ID AND module_ID=:module_ID",
                             {"class_ID": class_ID, "module_ID": module_ID}).fetchall()

    content_name = cur.execute("SELECT content_name FROM CONTENT WHERE class_ID=:class_ID AND module_ID=:module_ID",
                               {"class_ID": class_ID, "module_ID": module_ID}).fetchall()

    for content in content_ID:
        content_ID_list.append(list(content)[0])

    for content in content_name:
        content_name_list.append(list(content)[0])

    C = Tk()
    C.title("Edit Course")
    C.geometry("450x290")
    C.resizable(False, False)
    C.config(bg="#1b1b1b")

    def insert_content(content):
        with conn:
            cur.execute("INSERT INTO CONTENT VALUES (:content_ID, :content_name, :class_ID,"
                        " :file_path, :module_ID)",
                        {"content_ID": content.content_ID, "content_name": content.content_name,
                         "class_ID": content.class_ID, "file_path": content.absolute_path,
                         "module_ID": content.module_ID})

    def delete():
        ask_del = messagebox.askquestion("Delete Content", "Are you sure to delete this?")
        if ask_del == "yes":
            cur.execute("DELETE FROM CONTENT WHERE content_name=:content_name",
                        {"content_name": content_var.get()})
            conn.commit()
            C.destroy()
            messagebox.showinfo("Success", "The content has been deleted!")

    def add():
        filetypes = (
            ('text files', '*.*'),
            ('All files', '*.*')
        )
        file_abs_path = \
            filedialog.askopenfilename(title="Select a file", initialdir=module_path, filetypes=filetypes)

        save_ques = messagebox.askquestion("Add File?", "Are you sure to add this?")
        if save_ques == "yes":
            print(file_abs_path)
            from init import content

            rand_cont_ID = random.randint(10000, 50000)
            file_name = os.path.basename(file_abs_path).rsplit(".", 1)[0]

            if rand_cont_ID in content_ID_list:
                while rand_cont_ID in content_ID_list:
                    rand_cont_ID = random.randint(10000, 19999)

            new_content = content(rand_cont_ID, file_name, class_ID, file_abs_path, module_ID)
            insert_content(new_content)
            C.destroy()
            messagebox.showinfo("Success", "A new content has been successfully added!")

        else:
            print("You said no")

    content_var = StringVar()
    content_var.set(content_name_list[0])

    #   Text Display
    course_name_text = f"Module info: {module_name} - {module_ID}"

    #   Texts
    add_notice_lbl = Label(C, text="Press on ○ to add content", bg="#1b1b1b", fg="#F0E6FA")
    course_name_lbl = Label(C, text=course_name_text, bg="#1b1b1b", fg="#F0E6FA")
    add_new_content_lbl = Label(C, text="Add A New Content:", bg="#1b1b1b", fg="#F0E6FA")
    del_content_lbl = Label(C, text="Delete A Content:", bg="#1b1b1b", fg="#F0E6FA")

    #   Gap
    gap0 = Label(C, bg="#1b1b1b")
    gap1 = Label(C, bg="#1b1b1b")
    gap2 = Label(C, bg="#1b1b1b")
    gap3 = Label(C, bg="#1b1b1b")

    #   OptionMenu
    content_list_menu = OptionMenu(C, content_var, *content_name_list)

    #   Button
    get_file_path_btn = Button(C, text="○", command=add)
    del_content_btn = Button(C, text="Delete", command=delete)
    close_btn = Button(C, text="Close", command=C.destroy)

    #   Grid
    #   .grid(row=, column=)
    gap0.grid(row=0, column=0)
    course_name_lbl.grid(row=1, column=0, sticky=W)
    gap1.grid(row=2, column=0, pady=20)
    add_notice_lbl.grid(row=2, column=1, padx=120)
    add_new_content_lbl.grid(row=3, column=0, sticky=W)
    get_file_path_btn.grid(row=3, column=1)
    gap2.grid(row=4, column=0)
    del_content_lbl.grid(row=5, column=0, sticky=W)
    content_list_menu.grid(row=5, column=1)
    del_content_btn.grid(row=6, column=1, pady=10)
    gap3.grid(row=7, column=0)
    close_btn.grid(row=8, column=0, padx=10, sticky=W)

    C.mainloop()