from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk, ImageDraw
from datetime import *
import time 
from math import *
import sqlite3

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Sysytem")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        left_lbl = Label(self.root, bg="#08A3D2", bd=0)
        left_lbl.place(x=0, y=0, relheight=1,width=600)        

        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        login_frame =Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)

        title= Label(login_frame, text="Login Here", font=("roboto", 30, "bold"), bg="white", fg='#08A3D2').place(x=250, y=50)

        email= Label(login_frame, text="Email Address", font=("roboto", 18, "bold"), bg="white", fg='grey').place(x=250, y=150) 
        self.txt_email= Entry(login_frame, font=("roboto", 18), bg="light grey")
        self.txt_email.place(x=250, y=190, width=350, height=35)

        pass_= Label(login_frame, text="Password", font=("roboto", 18, "bold"), bg="white", fg='grey').place(x=250, y=250) 
        self.txt_pass_= Entry(login_frame, font=("roboto", 18), bg="light grey")
        self.txt_pass_.place(x=250, y=290, width=350, height=35)

        btn_reg=Button(login_frame, command=self.Register_window,  text="Register Account", font=("roboto", 14), bg="white", fg="#B00857", bd=0, cursor="hand2").place(x=242, y=330)

        btn_forget=Button(login_frame, command=self.forget_password_window,  text="Forget Password", font=("roboto", 14), bg="white", fg="#B00857", bd=0, cursor="hand2").place(x=450, y=330)

        btn_login=Button(login_frame, text="Login", command=self.login, font=("roboto", 20, "bold"), fg="white", bg="#B00857", cursor="hand2").place(x=350, y=400, width=180, height=40)

        self.lbl = Label(self.root, bg="#081923", bd=0)
        self.lbl.place(x=90, y=120, height=450, width=350)

        self.working()


    def forget_password(self):
        if self.cmb_question.get()=="--Select--" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
        else:
            try:
                con = sqlite3.connect('Employee.db')
                cur = con.cursor()
                cur.execute("SELECT * FROM  user_data where email=? AND question=? AND answer=?",(self.txt_email.get(), self.cmb_question.get(), self.txt_answer.get()))
                row = cur.fetchone()
                if row ==None:
                    messagebox.showerror("Error","Security question & answer not matched", parent=self.root2)
                else:
                    cur.execute("update user_data set password=? where email=?",(self.txt_new_pass.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Your password has been updated, Please login with your new password")
                    self.root2.destroy()
    
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to {str(es)}", parent=self.root)

    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error", "Please enter the email address to reset your password", parent=self.root)
        else:
            try:
                con = sqlite3.connect('Employee.db')
                cur = con.cursor()
                cur.execute("SELECT * FROM  user_data where email=?", (self.txt_email.get(),))
                row = cur.fetchone()
                if row ==None:
                    messagebox.showerror("Error","Please enter the valid email address to reset your password", parent=self.root)
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forgot password")
                    self.root2.geometry("400x400+450+150")
                    self.root2.configure(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t = Label(self.root2, text="Forgot Password", font=("roboto", 20, "bold"), bg="white", fg="red").place(x=0, y=10, relwidth=1)
                    
                    question= Label(self.root2, text="Security Question", font=("Sans Serif",15, "bold"), bg="white", fg="grey").place(x=80, y=100)        
                    self.cmb_question= ttk.Combobox(self.root2, font=("Roboto",12), state="readonly", justify="center")
                    self.cmb_question['value']=("--Select--","Your Pet Name","Your Birth Place", "Your Best Friend Name")
                    self.cmb_question.current(0)
                    self.cmb_question.place(x=80, y=130, width=250)

                    answer= Label(self.root2, text="Answer", font=("Sans Serif",15, "bold"), bg="white", fg="grey").place(x=80, y=180)   
                    self.txt_answer= Entry(self.root2, font=("Roboto",12), bg="light grey")
                    self.txt_answer.place(x=80, y=210, width=250)

                    new_password= Label(self.root2, text="New Password", font=("Sans Serif",15, "bold"), bg="white", fg="grey").place(x=80, y=260)        
                    self.txt_new_pass= Entry(self.root2, font=("Roboto",12), bg="light grey")
                    self.txt_new_pass.place(x=80, y=290, width=250)

                    btn_change_passwords = Button(self.root2, text="Reset Password", command=self.forget_password, bg="green", fg="white", font=("Roboto",15, "bold")).place(x=120, y= 340)
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to {str(es)}", parent=self.root)

    def Register_window(self):
        # self.root.quit()
        self.root.destroy()
        import Register

    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = sqlite3.connect('Employee.db')
                cur = con.cursor()
                cur.execute("SELECT * FROM  user_data where email=? AND password=?", (self.txt_email.get(), self.txt_pass_.get()))
                row = cur.fetchone()
                if row ==None:
                    messagebox.showerror("Error","Invalid email or password", parent=self.root)
                else:
                    messagebox.showinfo("Success","Welcome !!!")
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to {str(es)}", parent=self.root)

    def clock_image(self, hr, min_, sec_):
        clock =Image.new("RGB", (400, 400), (8,25,35))
        draw  = ImageDraw.Draw(clock)

        # Draw clock Image-----------------
        bg=Image.open("Image/c.png")
        bg=bg.resize((300,300), Image.ANTIALIAS)
        clock.paste(bg, (50,50))

        origin = 200,200
        # Draw Hour line Image-----------------
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))), fill="#DF005E", width=4)
        # Draw Minute line Image-----------------
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))), fill="white", width=3)
        # Draw Second line Image-----------------
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))), fill="yellow", width=2)
        # Draw circle Image-----------------
        draw.ellipse((195,195,210,210), fill="#1AD5D5")

        clock.save("Image/clock_new.png")

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h/12)*360
        min_ = (m/60)*360
        sec_ = (s/60)*360

        self.clock_image(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(file="Image/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)
     
root = Tk()
obj = Login_Window(root)
root.mainloop()