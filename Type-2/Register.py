from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        # self.root.config(bg="White")
        
        # Bg Image in Registration  Window
        self.bg=ImageTk.PhotoImage(file="Image/BG-Image.jpg")
        bg= Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        self.left=ImageTk.PhotoImage(file="Image/Side-Image.jpg")
        left= Label(self.root, image=self.left).place(x=40, y=100, width=465, height=520)

        # Register Frame
        frame1= Frame(self.root, bg="White")
        frame1.place(x=580, y=100, width=700, height=520)

        title= Label(frame1, text="REGISTER HERE", font=("Sans Serif",20, "bold"), bg="white", fg="green").place(x=50, y=30)

        # self.var_f_name = StringVar()
        f_name= Label(frame1, text="First Name", font=("Sans Serif",15, "bold"), bg="white", fg="grey").place(x=50, y=100)        
        self.txt_f_name= Entry(frame1, font=("Roboto",12), bg="light grey")
        self.txt_f_name.place(x=50, y=130, width=200)     

        l_name= Label(frame1, text="Last Name", font=("Sans Serif",15, "bold"), bg="white", fg="grey").place(x=370, y=100)        
        self.txt_l_name= Entry(frame1, font=("Roboto",12), bg="light grey")
        self.txt_l_name.place(x=370, y=130, width=200) 

        contact= Label(frame1, text="Contact No", font=("Sans Serif",15, "bold"), bg="white", fg="grey").place(x=50, y=170)        
        self.txt_contact= Entry(frame1, font=("Roboto",12), bg="light grey")
        self.txt_contact.place(x=50, y=200, width=200)         

        email= Label(frame1, text="Email ID", font=("Sans Serif",15, "bold"), bg="white", fg="grey").place(x=370, y=170)        
        self.txt_email= Entry(frame1, font=("Roboto",12), bg="light grey")
        self.txt_email.place(x=370, y=200, width=200)

        question= Label(frame1, text="Security Question", font=("Sans Serif",15, "bold"), bg="white", fg="grey").place(x=50, y=240)
        self.cmb_question= ttk.Combobox(frame1, font=("Roboto",12), state="readonly", justify="center")
        self.cmb_question['value']=("--Select--","Your Pet Name","Your Birth Place", "Your Best Friend Name")
        self.cmb_question.current(0)
        self.cmb_question.place(x=50, y=270, width=200)

        answer= Label(frame1, text="Answer", font=("Sans Serif",15, "bold"), bg="white", fg="grey").place(x=370, y=240)  
        self.txt_answer= Entry(frame1, font=("Roboto",12), bg="light grey")
        self.txt_answer.place(x=370, y=270, width=200) 

        password= Label(frame1, text="Password", font=("Sans Serif",15, "bold"), bg="white", fg="grey").place(x=50, y=310)        
        self.txt_password= Entry(frame1, font=("Roboto",12), bg="light grey", show="*")
        self.txt_password.place(x=50, y=340, width=200)         

        C_Paasword= Label(frame1, text="Confirm Password", font=("Sans Serif",15, "bold"), bg="white", fg="grey").place(x=370, y=310)        
        self.txt_C_Paasword= Entry(frame1, font=("Roboto",12), bg="light grey", show="*")
        self.txt_C_Paasword.place(x=370, y=340, width=200) 

        self.var_chk=IntVar()
        chk = Checkbutton(frame1, text="I agree the terms & condition", variable=self.var_chk, onvalue=1, offvalue=0, bg="White", font=("Roboto",12,"bold")).place(x=50, y=380) 

        self.btn_img=ImageTk.PhotoImage(file="Image/Register-Now.png")
        btn_register = Button(frame1, image=self.btn_img, bd=0, cursor="hand2", command=self.register_data).place(x=250, y=420)

        self.btn_img2=ImageTk.PhotoImage(file="Image/Login.png")
        btn_login = Button(root, image=self.btn_img2, bd=0, cursor="hand2", command=self.Login_window).place(x=40, y=20)  

    def Login_window(self):
        self.root.destroy()
        # self.root.quit()
        import Login

    def clear(self):
        self.txt_f_name.delete(0, END)
        self.txt_l_name.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_C_Paasword.delete(0, END)
        self.cmb_question.current(0)

    def register_data(self):
        if self.txt_f_name.get()=="" or self.txt_l_name.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_question.get()=="--Select--" or self.txt_answer.get()=="" or  self.txt_password.get()=="" or self.txt_C_Paasword.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_password.get()!=self.txt_C_Paasword.get():
            messagebox.showerror("Error", "Password & Confirm do not match", parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Please agree to the terms & conditions", parent=self.root)
        else:         
            try:
                con = sqlite3.connect('Employee.db')
                cur = con.cursor()
                print("Successfully Connected to SQLite")

                sql = f'''insert into user_data (f_name, l_name, contact, email, question, answer, password) values (?,?,?,?,?,?,?)'''
                
                data = (
                    self.txt_f_name.get(),
                    self.txt_l_name.get(),
                    self.txt_contact.get(),
                    self.txt_email.get(),
                    self.cmb_question.get(),
                    self.txt_answer.get(),
                    self.txt_password.get()
                )

                insert = cur.execute(sql, data)
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Register successfully", parent=self.root)
                self.clear()
            except Exception as e:
                print(e)
                messagebox.showerror("Error", f"error due to {str(e)}", parent=self.root)

root = Tk()
obj = Register(root)
root.mainloop()