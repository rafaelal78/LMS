from tkinter import *
import sqlite3
from tkPDFViewer import tkPDFViewer as pdf
from PIL import ImageTk, Image

def student_win(ID):
    conn = sqlite3.connect("IP.db")
    cur = conn.cursor()

    SP = Tk()
    SP.title("Student Window")
    SP.geometry("800x700")
    SP.resizable(False, False)
    SP.config(bg="#1b1b1b")

    #   pdfViewer
    display_schedule = pdf.ShowPdf().pdf_view(SP,
    pdf_location=r"C:\Users\lenovo\PycharmProjects\LMS\Images\FT-CU-CS-EH-321-OSD_AD_IP_ECS2_Nov-2021-8.pdf",
                                              width=75, height=40, bar=False)

    #   Image
    user_image = ImageTk.PhotoImage(Image.open("Images/user_1.png"))
    course_image = ImageTk.PhotoImage(Image.open("Images/courses_1.jpg"))
    logout_image = ImageTk.PhotoImage(Image.open("Images/logout_1.png"))

    def user_click():
        from Personal_details_window import personal_details
        personal_details(ID)

    def courses_click():
        SP.destroy()
        conn.close()
        from Modules import courses_window
        courses_window(ID)

    # def schedule_click():
    #     print("You clicked on schedule")

    def logout_click():
        SP.destroy()
        conn.close()
        from login_window import login_win
        login_win()

    #   LabelFrame
    user_FN = LabelFrame(SP, text="User", bg="#1b1b1b", fg="#F0E6FA")
    course_FN = LabelFrame(SP, text="Modules", bg="#1b1b1b", fg="#F0E6FA")
    # schedule_FN = LabelFrame(SP, text="Schedule")
    logout_FN = LabelFrame(SP, text="Logout", bg="#1b1b1b", fg="#F0E6FA")

    #   Button
    user_button = Button(user_FN, image=user_image, width=150, height=100, command=user_click)
    course_button = Button(course_FN, image=course_image, width=150, height=100, command=courses_click)
    # schedule_button = Button(schedule_FN, image=schedule_image, width=150, height=100, command=schedule_click)
    logout_button = Button(logout_FN, image=logout_image, width=150, height=100, command=logout_click)

    #   Grid
    user_FN.grid(row=0, column=0, sticky=W, columnspan=1)
    display_schedule.grid(row=0, column=1, rowspan=10)
    course_FN.grid(row=1, column=0, columnspan=1, sticky=W)
    # schedule_FN.grid(row=2, column=0, columnspan=1, sticky=W)
    logout_FN.grid(row=2, column=0, columnspan=1, sticky=W)

    user_button.grid(row=0, column=0)
    course_button.grid(row=0, column=0)
    # schedule_button.grid(row=0, column=0)
    logout_button.grid(row=0, column=0)

    SP.mainloop()

