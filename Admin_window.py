from tkinter import *
import sqlite3


def administrator_win(ID):
    conn = sqlite3.connect("IP.db")
    cur = conn.cursor()

    admin_username = cur.execute("SELECT username FROM USER WHERE user_ID=:user_ID",
                                 {"user_ID": ID}).fetchone()[0]
    admin_fullname = cur.execute("SELECT fullname FROM USER WHERE user_ID=:user_ID",
                                {"user_ID": ID}).fetchone()[0]

    AP = Tk()
    AP.title("Administrator Window")
    AP.geometry("370x430")
    AP.resizable(False, False)
    AP.config(bg="#1b1b1b")

    def create_user():
        AP.destroy()
        conn.close()
        from admin_create_user import create_user
        create_user(ID)

    def edit_User():
        AP.destroy()
        conn.close()
        from admin_edit_user import edit_user
        edit_user(ID)

    def edit_pers_info():
        from Personal_details_window import personal_details
        personal_details(ID)

    def logout():
        AP.destroy()
        conn.close()
        from login_window import login_win
        login_win()

    #   Text Displays
    user_ID_display = f"User ID: {ID}"
    username_display = f"Username: {admin_username}"
    fullname_display = f"Fullname: {admin_fullname}"

    #   Texts
    admin_ID_text = Label(AP, text=user_ID_display, bg="#1b1b1b", fg="#F0E6FA")
    admin_username_text = Label(AP, text=username_display, bg="#1b1b1b", fg="#F0E6FA")
    admin_fullname_text = Label(AP, text=fullname_display, bg="#1b1b1b", fg="#F0E6FA")

    #   Gaps
    blank0 = Label(AP, bg="#1b1b1b")
    blank1 = Label(AP, bg="#1b1b1b")
    blank2 = Label(AP, bg="#1b1b1b")
    blank3 = Label(AP, bg="#1b1b1b")
    blank4 = Label(AP, bg="#1b1b1b")

    #   Buttons
    create_user_button = Button(AP, text="Create User", pady=20, width=50, command=create_user)
    edit_user_button = Button(AP, text="Edit User", pady=20, width=50, command=edit_User)
    personal_info_button = Button(AP, text="Edit Personal Information", pady=20, width=50, command=edit_pers_info)
    logout_button = Button(AP, text="Logout", pady=20, width=50, command=logout)

    #   Grids
    blank0.grid(row=0, column=0)
    admin_ID_text.grid(row=1, column=0, sticky=W)
    admin_username_text.grid(row=2, column=0, sticky=W)
    admin_fullname_text.grid(row=3, column=0, sticky=W)
    blank1.grid(row=4, column=0)
    create_user_button.grid(row=5, column=0, padx=5)
    blank2.grid(row=6, column=0)
    edit_user_button.grid(row=7, column=0, padx=5)
    blank3.grid(row=8, column=0)
    personal_info_button.grid(row=9, column=0, padx=5)
    blank4.grid(row=10, column=0)
    logout_button.grid(row=11, column=0, padx=5)

    AP.mainloop()