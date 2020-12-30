import os
import ctypes
import tkinter as tk
from PIL import Image, ImageTk

ctypes.windll.shcore.SetProcessDpiAwareness(1)
cwd = os.getcwd()

class Main_Frame:

    def __init__(self, parent):
        self.parent = parent
        self.define_frames()
        self.generate_widgets()
        self.generate_layout()

    def define_frames(self):
        self.frm_top    =  tk.Frame(self.parent, bg="#0384fc")
        self.frm_middle =  tk.Frame(self.parent, bg="#0384fc")
        self.frm_logo   =  tk.Frame(self.frm_middle, bg="#0384fc")
        self.frm_login  =  tk.Frame(self.frm_middle, bg="#0384fc")
        self.frm_bottom =  tk.Frame(self.parent, bg="#0384fc")

    def generate_widgets(self):
        self.lbl_signin = tk.Label(
            self.frm_login, text="Sign in", bg="#0384fc", fg="white", 
            anchor=tk.W, font="Arial 12 bold"
        )

        img = Image.open(cwd + r'\logo.png')
        img = img.resize((150, 150), Image.ANTIALIAS)
        self.img_logo = ImageTk.PhotoImage(img)
        self.lbl_logo = tk.Label(self.frm_logo, image=self.img_logo, bg="#0384fc")

        self.frm_btn_signin = tk.Frame(
            self.frm_login,
            highlightbackground="white",
            highlightcolor="white",
            highlightthickness=3,
            bd=0
        )
        self.btn_signin = tk.Button(
            self.frm_btn_signin, text="Sign in", command=self.login, fg="white", font="Arial 9 bold",
            bg="#0384fc", activebackground="#0384fc", borderwidth=0,
            width=10, relief="solid"
        )

        self.txt_email_id = tk.Entry(
            self.frm_login, width=30, relief="solid", borderwidth=0
        )
        self.txt_passcode = tk.Entry(
            self.frm_login, show="*", width=30, relief="solid", borderwidth=0
        )

        self.lbl_grbg_top    = tk.Label(self.frm_top, bg="#0384fc")
        self.lbl_grbg_bottom = tk.Label(self.frm_bottom, bg="#0384fc")

    def generate_layout(self):
        self.frm_middle.columnconfigure(2, weight=2)
        self.frm_middle.columnconfigure((0, 1, 3), weight=1)

        self.frm_logo.grid(row=1, column=1)
        self.frm_login.grid(row=1, column=2)

        self.lbl_logo.pack()
        self.lbl_logo.image = self.img_logo

        self.lbl_signin.grid(row=0, column=0, pady=5, sticky=tk.W)
        self.txt_email_id.grid(row=1, column=0, pady=5, ipady=3)
        self.txt_passcode.grid(row=2, column=0, pady=5, ipady=3)
        self.frm_btn_signin.grid(row=3, column=0, pady=5, sticky=tk.E)
        self.btn_signin.pack()

        self.lbl_grbg_top.pack()
        self.lbl_grbg_bottom.pack()

        self.frm_top.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.frm_middle.pack(fill=tk.X)
        self.frm_bottom.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)


    def login(self):
        email    =  self.txt_email_id.get()
        passcode =  self.txt_passcode.get()

        if not any([not self.txt_email_id.get(), self.txt_passcode.get()]):
            return False
        if email == 'admin@xyz.com' and passcode == "password":
            print("Login Successful")
            return True

    def on_exit(self):
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Tk Login App")
    root.geometry("660x389")
    root.configure(bg = "")
    root.resizable(height = False, width = False)
    win_login = Main_Frame(root)
    root.mainloop()