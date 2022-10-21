import random
from tkinter import *
import sqlite3
from tkinter import messagebox

def create_user(ID):
    conn = sqlite3.connect('IP.db')
    cur = conn.cursor()

    ACU = Tk()
    ACU.title("Administrator Create User")
    ACU.geometry("460x300")
    ACU.resizable(False, False)
    ACU.config(bg="#1b1b1b")

    def add_user(user):
        with conn:
            cur.execute("INSERT INTO USER VALUES (:user_ID, :user_type, :fullname, :username, :password)",
                        {'user_ID': user.user_ID, 'user_type': user.user_type, "fullname": user.fullname,
                         'username': user.username, 'password': user.password})

    def link_user_class(user):
        with conn:
            cur.execute("INSERT INTO CLASS VALUES(:class_ID, :user_ID)",
                        {"class_ID": user.class_ID, "user_ID": user.user_ID})

    def register_new_user(event):
        Label(ACU, text="                                                      ", bg="#1b1b1b").grid(row=4, column=1)
        Label(ACU, text="                                                      ", bg="#1b1b1b").grid(row=6, column=1)
        Label(ACU, text="                                                      ", bg="#1b1b1b").grid(row=8, column=1)
        Label(ACU, text="                                                      ", bg="#1b1b1b").grid(row=10, column=1, sticky=N)

        if user_class_entry.get() == "":
            Label(ACU, text="Enter The User's Class", fg="red", bg="#1b1b1b").grid(row=4, column=1)

        if fullname_entry.get() == "":
            Label(ACU, text="Enter The User's Fullname", fg="red", bg="#1b1b1b").grid(row=6, column=1)

        if password_entry.get() == "":
            Label(ACU, text="Enter User's Password", fg="red", bg="#1b1b1b").grid(row=8, column=1)

        if confirm_password_entry.get() == "":
            Label(ACU, text="Confirm Password", fg="red", bg="#1b1b1b").grid(row=10, column=1, sticky=N)

        if fullname_entry.get() != "" and user_class_entry.get() != ""\
                and password_entry.get() != "" and confirm_password_entry.get() != "":
            if password_entry.get() == confirm_password_entry.get():

                if user_types_var.get() == "Admin":
                    user_ID = random.randint(0, 999)
                elif user_types_var.get() == "Student":
                    user_ID = random.randint(1001, 4999)
                else:
                    user_ID = random.randint(5000, 9999)

                try:
                    ver_user_ID = cur.execute("SELECT user_ID FROM USER WHERE user_ID=:user_ID",
                                              {"user_ID": user_ID}).fetchone()[0]

                    while ver_user_ID == user_ID:
                        if user_types_var.get() == "Admin":
                            user_ID = random.randint(0, 999)
                        elif user_types_var.get() == "Student":
                            user_ID = random.randint(1001, 4999)
                        else:
                            user_ID = random.randint(5000, 9999)
                except:
                    pass

                char_list = []

                fullname_in = fullname_entry.get()

                for char in fullname_in:
                    char_list.append(char)

                if ' ' in char_list:
                    user_name = f"{fullname_in.replace(' ', '_')}.{user_ID}"
                else:
                    user_name = f"{fullname_in}.{user_ID}"

                from init import user, Class

                class_user = Class(user_class_entry.get(), user_ID)
                new_user = user(user_ID, user_types_var.get(),
                                fullname_entry.get().title(),
                                user_name, password_entry.get())

                print(user_name)
                link_user_class(class_user)
                add_user(new_user)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "User Created")
                ACU.destroy()
                from Admin_window import administrator_win
                administrator_win(ID)

            else:
                Label(ACU, text="Enter User's Password", fg="red", bg="#1b1b1b").grid(row=8, column=1)
                Label(ACU, text="Confirm Password", fg="red", bg="#1b1b1b").grid(row=10, column=1, sticky=N)
        else:
            pass

    def back():
        conn.close()
        ACU.destroy()
        from Admin_window import administrator_win
        administrator_win(ID)

    #   Misc.
    user_types_list = ["Admin", "Student", "Teacher"]
    user_types_var = StringVar()
    user_types_var.set(user_types_list[1])

    #   OptionMenu
    user_types_opt = OptionMenu(ACU, user_types_var, *user_types_list)

    #   Texts
    user_type_text = Label(ACU, text="User Type:", bg="#1b1b1b", fg="#F0E6FA")
    user_class_text = Label(ACU, text="User class:", bg="#1b1b1b", fg="#F0E6FA")
    fullname_text = Label(ACU, text="Fullname:", bg="#1b1b1b", fg="#F0E6FA")
    password = Label(ACU, text="Password:", bg="#1b1b1b", fg="#F0E6FA")
    confirm_password = Label(ACU, text="Confirm Password:", bg="#1b1b1b", fg="#F0E6FA")

    #   Gaps
    gap0 = Label(ACU, bg="#1b1b1b")
    gap1 = Label(ACU, bg="#1b1b1b")
    gap2 = Label(ACU, bg="#1b1b1b")
    gap3 = Label(ACU, bg="#1b1b1b")
    gap4 = Label(ACU, bg="#1b1b1b")
    gap5 = Label(ACU, bg="#1b1b1b")

    #   Entries
    user_class_entry = Entry(ACU, width=55)
    fullname_entry = Entry(ACU, width=55)
    password_entry = Entry(ACU, width=55, show="*")
    confirm_password_entry = Entry(ACU, width=55, show="*")

    #   Buttons
    back_button = Button(ACU, text="Back", command=back)
    confirm_button = Button(ACU, text="Confirm", command=lambda: register_new_user("Bobby"))

    ACU.bind("<Return>", register_new_user)

    #   Grids
    gap0.grid(row=0, column=0)
    user_type_text.grid(row=1, column=0, sticky=W)
    user_types_opt.grid(row=1, column=1)
    gap1.grid(row=2, column=0)
    user_class_text.grid(row=3, column=0, sticky=W)
    user_class_entry.grid(row=3, column=1)
    gap2.grid(row=4, column=0)
    fullname_text.grid(row=5, column=0, sticky=W)
    fullname_entry.grid(row=5, column=1)
    gap3.grid(row=6, column=0)
    password.grid(row=7, column=0, sticky=W)
    password_entry.grid(row=7, column=1)
    gap4.grid(row=8, column=0)
    confirm_password.grid(row=9, column=0, sticky=W)
    confirm_password_entry.grid(row=9, column=1)
    gap5.grid(row=10, column=0, pady=10)
    back_button.grid(row=11, column=0)
    confirm_button.grid(row=11, column=1)

    ACU.mainloop()