from tkinter import *
import sqlite3

def retrieve_PW_win():
    RPW = Tk()
    RPW.geometry("360x210")
    RPW.resizable(False, False)
    RPW.title("Recover Account")
    RPW.config(bg="#1b1b1b")

    conn = sqlite3.connect("IP.db")
    cur = conn.cursor()

    def display_pas(event):
        Label(RPW, text="                                            ", bg="#1b1b1b").grid(row=2, column=1, sticky=N)

        username_list = []
        get_all_username = cur.execute("SELECT username FROM USER").fetchall()

        for username in get_all_username:
            username_list.append(list(username)[0])

        if username_entry.get()!= "":
            if username_entry.get() in username_list:
                get_pas = cur.execute("SELECT password FROM USER WHERE username=:username",
                                                         {"username": username_entry.get()}).fetchone()[0]
                from tkinter import messagebox
                messagebox.showinfo("Retrieved!", get_pas)
                RPW.destroy()
            else:
                Label(RPW, text="Invalid Username", fg="red", bg="#1b1b1b").grid(row=2, column=1, sticky=N)
        else:
            Label(RPW, text="Enter Username", fg="red", bg="#1b1b1b").grid(row=2, column=1, sticky=N)

    #   Texts
    username_text = Label(RPW, text="Username", bg="#1b1b1b", fg="#F0E6FA")

    #   Gaps
    blank0 = Label(RPW, bg="#1b1b1b", fg="#F0E6FA")
    blank1 = Label(RPW, bg="#1b1b1b", fg="#F0E6FA")

    #   Entries
    username_entry = Entry(RPW, width=45)

    #   Buttons
    close_button = Button(RPW, text="Close", command=RPW.destroy)
    confirm_button = Button(RPW, text="Confirm", command=lambda: display_pas("None"))

    #   Misc.
    RPW.bind("<Return>", display_pas)

    #   Grids
    blank0.grid(row=0, column=0, pady=30)
    username_text.grid(row=1,column=0, sticky=W)
    username_entry.grid(row=1, column=1)
    blank1.grid(row=2, column=0, pady=20)
    close_button.grid(row=3, column=0)
    confirm_button.grid(row=3, column=1)

    RPW.mainloop()