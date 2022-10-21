from tkinter import *
from PIL import ImageTk, Image
import sqlite3

def login_win():
    conn = sqlite3.connect('IP.db')
    cur = conn.cursor()

    login = Tk()
    login.title("Login")
    login.geometry("500x530")
    login.resizable(False, False)
    login.config(bg="#1b1b1b")

    logo = ImageTk.PhotoImage(Image.open("Images/login_image.png"))

    def login_command(event):
        Label(login, text="                                             ", bg="#1b1b1b").grid(row=2, column=1, sticky=N)
        Label(login, text="                                             ", bg="#1b1b1b").grid(row=4, column=1, sticky=N)

        if user_name_entry.get() == "":
            Label(login, text="Enter Your Username", fg="red", bg="#1b1b1b").grid(row=2, column=1, sticky=N)

        if password_entry.get() == "":
            Label(login, text="Enter your Password", fg="red", bg="#1b1b1b").grid(row=4, column=1, sticky=N)

        if user_name_entry.get() != "" and password_entry.get() != "":

            get_username = cur.execute("SELECT username FROM USER WHERE username=:username",
                                       {'username': user_name_entry.get()}).fetchone()

            try:
                if user_name_entry.get() == get_username[0] and get_username[0] != None:
                    get_password = cur.execute("SELECT password FROM USER WHERE password=:password",
                                               {'password': password_entry.get()}).fetchone()
                    try:
                        if password_entry.get() == get_password[0] and get_password[0] != None:
                            get_user_type = cur.execute("SELECT user_type FROM USER WHERE username=:username",
                                                        {"username": user_name_entry.get()}).fetchone()[0]
                            get_user_ID = cur.execute("SELECT user_id FROM USER WHERE username=:username",
                                                      {"username": user_name_entry.get()}).fetchone()[0]

                            if get_user_type == "Admin":
                                login.destroy()
                                conn.close()
                                from Admin_window import administrator_win
                                administrator_win(get_user_ID)
                            elif get_user_type == "Student":
                                login.destroy()
                                conn.close()
                                from Stud_window import student_win
                                student_win(get_user_ID)
                            else:
                                login.destroy()
                                conn.close()
                                from Lect_window import teacher_window
                                teacher_window(get_user_ID)
                    except:
                        Label(login, text="Invalid Password", fg="red", bg="#1b1b1b").grid(row=4, column=1, sticky=N)
            except:
                Label(login, text="Invalid Username", fg="red", bg="#1b1b1b").grid(row=2, column=1, sticky=N)
        else:
            pass

    def forgot_PW(event):
        from retrieve_password_window import retrieve_PW_win
        retrieve_PW_win()

    #   Texts
    user_name_text = Label(login, text="Username", bg="#1b1b1b", fg="#F0E6FA")
    password_text = Label(login, text="Password", bg="#1b1b1b", fg="#F0E6FA")
    forgot_password_clickable_text = Label(login, text="Forgot Password? Click Here", bg="#1b1b1b", fg="#F0E6FA")

    #   Gaps
    blank0 = Label(login, bg="#1b1b1b", fg="#F0E6FA")
    blank1 = Label(login, bg="#1b1b1b", fg="#F0E6FA")
    blank2 = Label(login, bg="#1b1b1b", fg="#F0E6FA")
    blank3 = Label(login, bg="#1b1b1b", fg="#F0E6FA")

    #   Entries
    user_name_entry = Entry(login, width=55)
    password_entry = Entry(login, width=55, show="*")

    #   Buttons
    login_button = Button(login, text="Login", command=lambda: login_command(1))

    #   Binds
    forgot_password_clickable_text.bind("<Button-1>", forgot_PW)

    #   Misc.
    display_logo = Label(login, image=logo, bg="#1b1b1b")
    login.bind("<Return>", login_command)

    #   Grids
    display_logo.grid(row=0, column=0, padx=170, pady=50, columnspan=100)
    user_name_text.grid(row=1, column=0, sticky=W)
    user_name_entry.grid(row=1, column=1)
    blank0.grid(row=2, column=0, pady=10)
    password_text.grid(row=3, column=0, sticky=W)
    password_entry.grid(row=3, column=1)
    blank1.grid(row=4, column=0, pady=10)

    login_button.grid(row=5, column=1)

    blank2.grid(row=6, column=1, pady=20)
    forgot_password_clickable_text.grid(row=7, column=0, columnspan=3, sticky=W)
    blank3.grid(row=8, column=0, pady=10)

    login.mainloop()
