from tkinter import *
import sqlite3
from tkinter import messagebox

def personal_details(ID):
    conn = sqlite3.connect("IP.db")
    cur = conn.cursor()

    # user_type = cur.execute("SELECT user_type FROM USER WHERE user_ID=:user_ID",
    #                         {"user_ID": ID}).fetchone()[0]
    try:
        user_class = cur.execute("SELECT class_ID FROM CLASS WHERE user_ID=:user_ID",
                            {"user_ID": ID}).fetchone()[0]
    except:
        user_class = "None"
    fullname = cur.execute("SELECT fullname FROM USER WHERE user_ID=:user_ID",
                                 {"user_ID": ID}).fetchone()[0]
    username = cur.execute("SELECT username FROM USER WHERE user_ID=:user_ID",
                           {"user_ID": ID}).fetchone()[0]
    user_password = cur.execute("SELECT password FROM USER WHERE user_ID=:user_ID",
                           {"user_ID": ID}).fetchone()[0]

    PD = Tk()
    PD.title("User details")
    PD.geometry("390x310")
    PD.resizable(False, False)
    PD.config(bg="#1b1b1b")

    def change_username():
        CUN = Toplevel()
        CUN.geometry("440x150")
        CUN.resizable(False, False)
        CUN.title("Edit Username")
        CUN.config(bg="#1b1b1b")

        def confirm_change(event):
            Label(CUN, text="                              ", bg="#1b1b1b", fg="#F0E6FA").grid(row=4, column=1)
            if new_username_entry.get() != "":
                response = messagebox.askyesno("Confirm Change?", "Are you sure to make the change?")
                if response == 1:
                    with conn:
                        cur.execute("""UPDATE USER SET username=:username
                                    WHERE user_id=:user_id""", {'user_id': ID, 'username': new_username_entry.get()})
                    messagebox.showinfo("Success!", "Username successfully changed!")
                    CUN.destroy()
                    PD.destroy()
                    personal_details(ID)
                else:
                    pass
            else:
                Label(CUN, text="Enter A New Username", fg="red", bg="#1b1b1b").grid(row=4, column=1)

        #   Text Displays
        cur_username = f"Current Username {username}"

        #   Texts
        current_username_text = Label(CUN, text=cur_username, bg="#1b1b1b", fg="#F0E6FA")
        new_username_text = Label(CUN, text="New Username:", bg="#1b1b1b", fg="#F0E6FA")

        #   Gaps
        gap_0 = Label(CUN, bg="#1b1b1b")
        gap_1 = Label(CUN, bg="#1b1b1b")
        gap_2 = Label(CUN, bg="#1b1b1b")

        #   Entries
        new_username_entry = Entry(CUN, width=55)

        #   Buttons
        confirm_button = Button(CUN, text="Confirm", command=lambda: confirm_change("None"))
        close_button = Button(CUN, text="Close", command=CUN.destroy)

        #   Misc.
        CUN.bind("<Return>", confirm_change)

        #   Grids
        gap_0.grid(row=0, column=0)
        current_username_text.grid(row=1, column=0, columnspan=2, sticky=W)
        gap_1.grid(row=2, column=0)
        new_username_text.grid(row=3, column=0)
        new_username_entry.grid(row=3, column=1)
        gap_2.grid(row=4, column=0)
        close_button.grid(row=5, column=0)
        confirm_button.grid(row=5, column=1)

    def change_password():
        CPW = Toplevel()
        CPW.geometry("450x150")
        CPW.resizable(False, False)
        CPW.title("Verify Password")
        CPW.config(bg="#1b1b1b")

        def ver_PW(event):
            Label(CPW, text="                                                     ", bg="#1b1b1b").grid(row=2, column=1)
            Label(CPW, text="                                                     ", bg="#1b1b1b").grid(row=4, column=1, sticky=N)

            if current_password_entry.get() == "":
                Label(CPW, text="Enter Your Current Password", fg="red", bg="#1b1b1b").grid(row=2, column=1)

            if confirm_password_entry.get() == "":
                Label(CPW, text="Re-Enter Your Current Password", fg="red", bg="#1b1b1b").grid(row=4, column=1, sticky=N)

            if confirm_password_entry.get() != "" and current_password_entry.get() != "":
                if confirm_password_entry.get() == current_password_entry.get():
                    ver_password = cur.execute("SELECT password FROM USER WHERE user_id=:user_id",
                                               {"user_id": ID}).fetchone()[0]
                    if ver_password == confirm_password_entry.get():
                        CPW.destroy()
                        edit_password()
                    else:
                        Label(CPW, text="Invalid Password", fg="red", bg="#1b1b1b").grid(row=2, column=1)
                        Label(CPW, text="Invalid Password", fg="red", bg="#1b1b1b").grid(row=4, column=1, sticky=N)
                else:
                    Label(CPW, text="Both Passwords Don't Match", fg="red", bg="#1b1b1b").grid(row=2, column=1)
                    Label(CPW, text="Both Passwords Don't Match", fg="red", bg="#1b1b1b").grid(row=4, column=1, sticky=N)
            else:
                pass

        def edit_password():
            EP = Toplevel()
            EP.geometry("450x150")
            EP.resizable(False, False)
            EP.title("Change Password")
            EP.config(bg="#1b1b1b")

            def confirm_change(event):
                Label(EP, text="                                                     ", bg="#1b1b1b").grid(row=2, column=1)
                Label(EP, text="                                                     ", bg="#1b1b1b").grid(row=4, column=1, sticky=N)

                if new_password_entry.get() == "":
                    Label(EP, text="Enter A New Password", fg="red", bg="#1b1b1b").grid(row=2, column=1)

                if confirm_new_password_entry.get() == "":
                    Label(EP, text="Re-Enter Your New Password", fg="red", bg="#1b1b1b").grid(row=4, column=1, sticky=N)

                if new_password_entry.get() != "" and confirm_new_password_entry.get() != "":
                    if new_password_entry.get() == confirm_new_password_entry.get():
                        response = messagebox.askyesno("Confirm Change?", "Are you sure to make the change?")
                        if response == 1:
                            with conn:
                                cur.execute("""UPDATE USER SET password=:password
                                                                    WHERE user_id=:user_id""",
                                            {'user_id': ID, 'password': new_password_entry.get()})
                                conn.commit()
                                messagebox.showinfo("Success!", "Password successfully changed!")
                                EP.destroy()
                                PD.destroy()
                                personal_details(ID)
                    else:
                        Label(EP, text="Both Passwords Don't Match", fg="red", bg="#1b1b1b").grid(row=2, column=1)
                        Label(EP, text="Both Passwords Don't Match", fg="red", bg="#1b1b1b").grid(row=4, column=1, sticky=N)
                else:
                    pass

            #   Texts
            new_password_text = Label(EP, text="New Password:", bg="#1b1b1b", fg="#F0E6FA")
            confirm_new_password_text = Label(EP, text="Confirm password:", bg="#1b1b1b", fg="#F0E6FA")

            #   Gaps
            gap__0 = Label(EP, bg="#1b1b1b")
            gap__1 = Label(EP, bg="#1b1b1b")
            gap__2 = Label(EP, bg="#1b1b1b")

            #   Entry
            new_password_entry = Entry(EP, width=55, show="*")
            confirm_new_password_entry = Entry(EP, width=55, show="*")

            #   Buttons
            close__button = Button(EP, text="Close", command=EP.destroy)
            confirm_button = Button(EP, text="Confirm", command=lambda: confirm_change("None"))

            #   Misc.
            EP.bind("<Return>", confirm_change)

            #   Grids
            gap__0.grid(row=0, column=0)
            new_password_text.grid(row=1, column=0, sticky=W)
            new_password_entry.grid(row=1, column=1)
            gap__1.grid(row=2, column=0)
            confirm_new_password_text.grid(row=3, column=0, sticky=W)
            confirm_new_password_entry.grid(row=3, column=1)
            gap__2.grid(row=4, column=0)
            close__button.grid(row=5, column=0)
            confirm_button.grid(row=5, column=1)

        #   Texts
        current_password_text = Label(CPW, text="Current Password:", bg="#1b1b1b", fg="#F0E6FA")
        confirm_password_text = Label(CPW, text="Confirm Password:", bg="#1b1b1b", fg="#F0E6FA")

        #   Gaps
        gap_0 = Label(CPW, bg="#1b1b1b")
        gap_1 = Label(CPW, bg="#1b1b1b")
        gap_2 = Label(CPW, bg="#1b1b1b")

        #   Entry
        current_password_entry = Entry(CPW, width=55, show="*")
        confirm_password_entry = Entry(CPW, width=55, show="*")

        #   Buttons
        close_button = Button(CPW, text="Close", command=CPW.destroy)
        verify_button = Button(CPW, text="Verify", command=lambda: ver_PW("None"))

        #   Misc.
        CPW.bind("<Return>", ver_PW)

        #   Grids
        gap_0.grid(row=0, column=0)
        current_password_text.grid(row=1, column=0, sticky=W)
        current_password_entry.grid(row=1, column=1)
        gap_1.grid(row=2, column=0)
        confirm_password_text.grid(row=3, column=0, sticky=W)
        confirm_password_entry.grid(row=3, column=1)
        gap_2.grid(row=4, column=0, pady=5)
        close_button.grid(row=5, column=0)
        verify_button.grid(row=5, column=1)

    #   Text Displays
    user_ID_display = f"User ID: {ID}"
    user_class_display = f"Class: {user_class}"
    fullname_display = f"Fullname: {fullname}"
    username_display = f"Username: {username}"
    password_display = "Password: " + str(len(user_password) * "*")

    #   Texts
    update_user_text = Label(PD, text="Press on ○ to update", bg="#1b1b1b", fg="#F0E6FA")
    user_ID_text = Label(PD, text=user_ID_display, bg="#1b1b1b", fg="#F0E6FA")
    user_class_text = Label(PD, text=user_class_display, bg="#1b1b1b", fg="#F0E6FA")
    username_text = Label(PD, text=username_display, bg="#1b1b1b", fg="#F0E6FA")
    fullname_text = Label(PD, text=fullname_display, bg="#1b1b1b", fg="#F0E6FA")
    password_text = Label(PD, text=password_display, bg="#1b1b1b", fg="#F0E6FA")

    #   Gaps
    gap0 = Label(PD, bg="#1b1b1b")
    gap1 = Label(PD, bg="#1b1b1b")
    gap2 = Label(PD, bg="#1b1b1b")
    gap3 = Label(PD, bg="#1b1b1b")
    gap4 = Label(PD, bg="#1b1b1b")
    gap5 = Label(PD, bg="#1b1b1b")

    #   Buttons
    change_username_btn = Button(PD, text="○", command=change_username)
    change_password_btn = Button(PD, text="○", command=change_password)
    back_button = Button(PD, text="Close", command=PD.destroy)

    #   Grids
    gap0.grid(row=0, column=0)
    update_user_text.grid(row=0, column=1, sticky=E, padx=120)
    user_ID_text.grid(row=1, column=0, sticky=W)
    gap1.grid(row=2, column=0)
    user_class_text.grid(row=3, column=0, sticky=W)
    gap2.grid(row=4, column=0)
    username_text.grid(row=5, column=0, sticky=W)
    change_username_btn.grid(row=5, column=1)
    gap3.grid(row=6, column=0)
    fullname_text.grid(row=7, column=0, sticky=W)
    gap4.grid(row=8, column=0)
    password_text.grid(row=9, column=0, sticky=W)
    change_password_btn.grid(row=9, column=1)
    gap5.grid(row=10, column=0, pady=15)
    back_button.grid(row=11, column=0, sticky=W, padx=5)

    PD.mainloop()