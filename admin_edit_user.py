from tkinter import *
import sqlite3
from tkinter import messagebox

def edit_user(ID):

    conn = sqlite3.connect("IP.db")
    cur = conn.cursor()

    stud_users = cur.execute("SELECT * FROM USER WHERE user_type=:user_type",
                             {"user_type": "Student"}).fetchall()

    lect_users = cur.execute("SELECT * FROM USER WHERE user_type=:user_type",
                             {"user_type": "Teacher"}).fetchall()

    tmp_user_list = []
    fullname_list = []
    user_id_list = []
    user_list = []

    for user in stud_users:
        tmp_user_list.append(list(user))
    for user in lect_users:
        tmp_user_list.append(list(user))

    for user in tmp_user_list:
        fullname_list.append(user[3])
    for user in tmp_user_list:
        user_id_list.append(user[0])

    for index in range(len(fullname_list)):
        user_list.append(f"{fullname_list[index]} - {user_id_list[index]}")

    EU = Tk()
    EU.title("Administrator User Management")
    EU.geometry("500x300")
    EU.resizable(False, False)
    EU.config(bg="#1b1b1b")

    def index_clicked(event):
        for i in user_LB.curselection():
            modify_user(tmp_ID_list[i])

    def search_user(event):
        user_LB.delete(0, END)
        key = search_entry.get()
        global tmp_list
        global tmp_ID_list
        tmp_list = []
        tmp_ID_list = []

        for elem in user_list:
            if key in elem:
                tmp_list.append(elem)

        for elem in tmp_list:
            for ID in user_id_list:
                if str(ID) in elem:
                    tmp_ID_list.append(ID)

        for index in range(len(tmp_list)):
            user_LB.insert(index, tmp_list[index])

    def modify_user(new_user_ID):

        user_class = cur.execute("SELECT class_ID FROM CLASS WHERE user_ID=:user_ID",
                                    {"user_ID": new_user_ID}).fetchone()[0]
        user_fullname = cur.execute("SELECT fullname FROM USER WHERE user_ID=:user_ID",
                                    {"user_ID": new_user_ID}).fetchone()[0]
        user_username = cur.execute("SELECT username FROM USER WHERE user_ID=:user_ID",
                                    {"user_ID": new_user_ID}).fetchone()[0]
        user_password = cur.execute("SELECT password FROM USER WHERE user_ID=:user_ID",
                                    {"user_ID": new_user_ID}).fetchone()[0]

        UC = Tk()
        UC.title("Administrator User Management")
        UC.geometry("400x290")
        UC.resizable(False, False)
        UC.config(bg="#1b1b1b")

        def modify_class():
            MF = Toplevel()
            MF.title("Modify User Class")
            MF.geometry("460x150")
            MF.config(bg="#1b1b1b")

            def change_class(event):
                Label(MF, text="                                                     ", bg="#1b1b1b").grid(row=2, column=1, sticky=N)
                if new_class_ent.get() != "":
                    response = messagebox.askyesno("Confirm Change?", "Are you sure to make the change?")
                    if response == 1:
                        with conn:
                            cur.execute("""UPDATE CLASS SET class_ID=:class_ID WHERE user_ID=:user_ID""",
                                        {'class_ID': new_class_ent.get(), 'user_ID': new_user_ID})
                            conn.commit()
                            messagebox.showinfo("Success!", "User Class Successfully Changed!")
                            MF.destroy()
                            UC.destroy()
                            EU.destroy()
                            edit_user(ID)
                else:
                    Label(MF, text="Enter User's Class", fg="red", bg="#1b1b1b").grid(row=2, column=1, sticky=N)

            #   Texts
            new_class_text = Label(MF, text="New User Class:", bg="#1b1b1b", fg="#F0E6FA")

            #   Gaps
            gap_0 = Label(MF, bg="#1b1b1b",)
            gap_1 = Label(MF, bg="#1b1b1b",)

            #   Entries
            new_class_ent = Entry(MF, width=55)

            #   Button
            confirm_btn = Button(MF, text="Confirm", command=lambda: change_class("None"))
            close_btn = Button(MF, text="Close", command=MF.destroy)

            #   Misc.
            MF.bind("<Return>", change_class)

            #   Grids
            gap_0.grid(row=0, column=0, pady=10)
            new_class_text.grid(row=1, column=0, sticky=W)
            new_class_ent.grid(row=1, column=1)
            gap_1.grid(row=2, column=0, pady=10)
            close_btn.grid(row=3, column=0)
            confirm_btn.grid(row=3, column=1)

        def modify_fullname():
            MF = Toplevel()
            MF.title("Modify User Fullname")
            MF.geometry("460x150")
            MF.config(bg="#1b1b1b")

            def change_fullname(event):
                Label(MF, text="                                                     ", bg="#1b1b1b").grid(row=2, column=1, sticky=N)
                if new_FN_ent.get() != "":
                    response = messagebox.askyesno("Confirm Change?", "Are you sure to make the change?")
                    if response == 1:
                        with conn:
                            cur.execute("""UPDATE USER SET fullname=:fullname WHERE user_ID=:user_ID""",
                                        {'fullname': new_FN_ent.get(), 'user_ID': new_user_ID})
                            conn.commit()
                            messagebox.showinfo("Success!", "User Fullname successfully changed!")
                            MF.destroy()
                            UC.destroy()
                            EU.destroy()
                            edit_user(ID)
                else:
                    Label(MF, text="Enter User's Fullname", fg="red", bg="#1b1b1b").grid(row=2, column=1, sticky=N)

            #   Texts
            new_FN_text = Label(MF, text="New User Fullname:", bg="#1b1b1b", fg="#F0E6FA")

            #   Gaps
            gap_0 = Label(MF, bg="#1b1b1b")
            gap_1 = Label(MF, bg="#1b1b1b")

            #   Entries
            new_FN_ent = Entry(MF, width=55)

            #   Button
            confirm_btn = Button(MF, text="Confirm", command=lambda: change_fullname("None"))
            close_btn = Button(MF, text="Close", command=MF.destroy)

            #   Misc.
            MF.bind("<Return>", change_fullname)

            #   Grids
            gap_0.grid(row=0, column=0, pady=10)
            new_FN_text.grid(row=1, column=0, sticky=W)
            new_FN_ent.grid(row=1, column=1)
            gap_1.grid(row=2, column=0, pady=10)
            close_btn.grid(row=3, column=0)
            confirm_btn.grid(row=3, column=1)

        def modify_username():
            MU = Toplevel()
            MU.geometry("440x150")
            MU.title("Modify Username")
            MU.resizable(False, False)
            MU.config(bg="#1b1b1b")

            def change_username(event):
                Label(MU, text="                                                     ", bg="#1b1b1b").grid(row=2, column=1, sticky=N)
                if new_UN_ent.get() != "":
                    response = messagebox.askyesno("Confirm Change?", "Are you sure to make the change?")
                    if response == 1:
                        with conn:
                            cur.execute("""UPDATE USER SET username=:username WHERE user_ID=:user_ID""",
                                        {'user_ID': new_user_ID, 'username': new_UN_ent.get()})
                            conn.commit()
                            messagebox.showinfo("Success!", "Username successfully changed!")
                            MU.destroy()
                            UC.destroy()
                            EU.destroy()
                            edit_user(ID)
                else:
                    Label(MU, text="Enter User's New Username", fg="red", bg="#1b1b1b").grid(row=2, column=1, sticky=N)

            #   Texts
            new_UN_text = Label(MU, text="New Username:", bg="#1b1b1b", fg="#F0E6FA")

            #   Gaps
            gap_0 = Label(MU, bg="#1b1b1b")
            gap_1 = Label(MU, bg="#1b1b1b")

            #   Entries
            new_UN_ent = Entry(MU, width=55)

            #   Button
            confirm_btn = Button(MU, text="Confirm", command=lambda: change_username("None"))
            close_btn = Button(MU, text="Close", command=MU.destroy)

            #   Misc.
            MU.bind("<Return>", change_username)

            #   Grids
            gap_0.grid(row=0, column=0, pady=10)
            new_UN_text.grid(row=1, column=0, sticky=W)
            new_UN_ent.grid(row=1, column=1)
            gap_1.grid(row=2, column=0, pady=10)
            close_btn.grid(row=3, column=0)
            confirm_btn.grid(row=3, column=1)

        def modify_password():
            MP = Toplevel()
            MP.geometry("460x205")
            MP.title("Modify User password")
            MP.resizable(False, False)
            MP.config(bg="#1b1b1b")

            def change_password(event):
                Label(MP, text="                                                     ", bg="#1b1b1b").grid(row=2, column=1, sticky=N)
                Label(MP, text="                                                     ", bg="#1b1b1b").grid(row=4, column=1, sticky=N)

                if new_PW_ent.get() == "":
                    Label(MP, text="Enter User's New Password", fg="red", bg="#1b1b1b").grid(row=2, column=1, sticky=N)
                if confirm_PW_ent.get() == "":
                    Label(MP, text="Confirm User's New Password", fg="red", bg="#1b1b1b").grid(row=4, column=1, sticky=N)

                if new_PW_ent.get() != "" and confirm_PW_ent.get() != "":
                    if new_PW_ent.get() == confirm_PW_ent.get():
                        response = messagebox.askyesno("Confirm Change?", "Are you sure to make the change?")
                        if response == 1:
                            with conn:
                                cur.execute("""UPDATE USER SET password=:password WHERE user_ID=:user_ID""",
                                            {'user_ID': new_user_ID, 'password': new_PW_ent.get()})
                                conn.commit()
                                messagebox.showinfo("Success!", "Password successfully changed!")
                                MP.destroy()
                                UC.destroy()
                                EU.destroy()
                                edit_user(ID)
                    else:
                        Label(MP, text="Passwords Don't Match", fg="red", bg="#1b1b1b").grid(row=4, column=1, sticky=N)
                else:
                    pass

            #   Texts
            new_PW_text = Label(MP, text="New User Password:", bg="#1b1b1b", fg="#F0E6FA")
            confirm_PW_text = Label(MP, text="Confirm Password:", bg="#1b1b1b", fg="#F0E6FA")

            #   Gaps
            gap_0 = Label(MP, bg="#1b1b1b")
            gap_1 = Label(MP, bg="#1b1b1b")
            gap_2 = Label(MP, bg="#1b1b1b")

            #   Entries
            new_PW_ent = Entry(MP, width=55)
            confirm_PW_ent = Entry(MP, width=55)

            #   Button
            confirm_btn = Button(MP, text="Confirm", command=lambda: change_password("None"))
            close_btn = Button(MP, text="Close", command=MP.destroy)

            #   Misc.
            MP.bind("<Return>", change_password)

            #   Grids
            gap_0.grid(row=0, column=0, pady=10)
            new_PW_text.grid(row=1, column=0)
            new_PW_ent.grid(row=1, column=1)
            gap_1.grid(row=2, column=0, pady=10)
            confirm_PW_text.grid(row=3, column=0)
            confirm_PW_ent.grid(row=3, column=1)
            gap_2.grid(row=4, column=0, pady=10)
            close_btn.grid(row=5, column=0)
            confirm_btn.grid(row=5, column=1)

        def delete_user():
            response = messagebox.askyesno("Delete User?", "Are you sure to delete this user?")
            if response == 1:
                with conn:
                    cur.execute("DELETE FROM USER WHERE user_ID=:user_ID", {"user_ID": new_user_ID})
                    conn.commit()
                    messagebox.showinfo("Deleted", "User Deleted!")
                    UC.destroy()
                    EU.destroy()
                    edit_user(ID)
            else:
                UC.destroy()

        #   Text Displays
        user_ID_display = f"User ID: {new_user_ID}"
        class_ID_display = f"User class: {user_class}"
        fullname_display = f"Fullname: {user_fullname}"
        username_display = f"Username: {user_username}"
        password_display = f"Password: {user_password}"

        #   Texts
        update_user_text = Label(UC, text="Press on ○ to update", bg="#1b1b1b", fg="#F0E6FA")
        user_ID_text = Label(UC, text=user_ID_display, bg="#1b1b1b", fg="#F0E6FA")
        user_class_text = Label(UC, text=class_ID_display, bg="#1b1b1b", fg="#F0E6FA")
        fullname_text = Label(UC, text=fullname_display, bg="#1b1b1b", fg="#F0E6FA")
        username_text = Label(UC, text=username_display, bg="#1b1b1b", fg="#F0E6FA")
        password_text = Label(UC, text=password_display, bg="#1b1b1b", fg="#F0E6FA")

        #   Gaps
        gap_0 = Label(UC, bg="#1b1b1b")
        gap_1 = Label(UC, bg="#1b1b1b")
        gap_2 = Label(UC, bg="#1b1b1b")
        gap_3 = Label(UC, bg="#1b1b1b")
        gap_4 = Label(UC, bg="#1b1b1b")

        #   Buttons
        change_class_btn = Button(UC, text="○", command=modify_class)
        change_fullname_btn = Button(UC, text="○", command=modify_fullname)
        change_username_btn = Button(UC, text="○", command=modify_username)
        change_password_btn = Button(UC, text="○", command=modify_password)
        back_btn = Button(UC, text="Close", command=UC.destroy)
        del_user_btn = Button(UC, text="Delete", command=delete_user)

        #   Grids
        update_user_text.grid(row=0, column=1, sticky=E, padx=120)
        user_ID_text.grid(row=1, column=0, sticky=W)
        gap_0.grid(row=2, column=0)
        user_class_text.grid(row=3, column=0, sticky=W)
        change_class_btn.grid(row=3, column=1)
        gap_1.grid(row=4, column=0)
        fullname_text.grid(row=5, column=0, sticky=W)
        change_fullname_btn.grid(row=5, column=1)
        gap_2.grid(row=6, column=0)
        username_text.grid(row=7, column=0, sticky=W)
        change_username_btn.grid(row=7, column=1)
        gap_3.grid(row=8, column=0)
        password_text.grid(row=9, column=0, sticky=W)
        change_password_btn.grid(row=9, column=1)
        gap_4.grid(row=10, column=0)
        back_btn.grid(row=11, column=0, sticky=W, padx=5)
        del_user_btn.grid(row=11, column=1, sticky=W)

        UC.mainloop()

    def back():
        EU.destroy()
        conn.close()
        from Admin_window import administrator_win
        administrator_win(ID)

    #   Texts
    search_text = Label(EU, text="Search:", bg="#1b1b1b", fg="#F0E6FA")

    #   Gaps
    gap0 = Label(EU, bg="#1b1b1b")
    gap1 = Label(EU, bg="#1b1b1b")
    gap2 = Label(EU, bg="#1b1b1b")

    #   Entry
    search_entry = Entry(EU, width=55)

    #   Listbox
    user_LB = Listbox(EU, width=55)

    #   Buttons
    back_button = Button(EU, text="Back", command=back)
    search_button = Button(EU, text="Search", command=lambda: search_user("None"))

    # Misc.
    user_LB.bind('<Double-Button-1>', index_clicked)
    EU.bind('<Return>', search_user)

    #   Grids
    gap0.grid(row=0, column=0)
    search_text.grid(row=1, column=0, padx=20, sticky=W)
    search_entry.grid(row=1, column=1)
    search_button.grid(row=1, column=2, padx=20)
    gap1.grid(row=2, column=0)
    user_LB.grid(row=3, column=1)
    gap2.grid(row=4, column=0)
    back_button.grid(row=5, column=0)

    EU.mainloop()
