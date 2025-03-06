from re import search
from tkinter import *
from Database import DB
from tkinter import messagebox
from Api import Api


class weatherApplication:
    def __init__(self):

        self.dbo=DB()

        self.apio=Api()         #apio object

        self.root=Tk()

        self.root.geometry("350x650")
        self.root.configure(bg="#4158D0")
        self.root.title("weather Application")
        self.login()
        self.root.mainloop()#to hold the GUI(graphic user interface)
    def clear(self):
        for i in self.root.slaves():
            i.destroy()

    def login(self):
        self.clear()

        heading=Label(self.root,text="Weather Apllication",bg="#4158D0",fg="white")
        heading.config(font=("Cambria",24,"italic","bold"))
        heading.pack(pady=(50,75))

        email_label=Label(self.root,text="Enter Email",bg="#4158D0",fg="White")
        email_label.config(font=("Cambria",16,"italic"))
        email_label.pack(pady=(5,5))
        self.email_input=Entry(self.root,width=25)
        self.email_input.config(font=("Cambria",16,"italic"))
        self.email_input.pack(pady=(5,25),ipady=1)

        password_label=Label(self.root,text="Enter password",bg="#4158D0",fg="White")
        password_label.config(font=("Cambria",16,"italic"))
        password_label.pack(pady=(5,5))

        self.password_input=Entry(self.root,width=25,show="*")
        self.password_input.config(font=("Cambria",16,"italic"))
        self.password_input.pack(pady=(5,50),ipady=1)

        login_btn=Button(self.root,text="Login",width=10,command=self.perform_login)
        login_btn.config(font=("Cambria",16,"italic"))
        login_btn.pack(pady=(5,5))

        member_label=Label(self.root,text="Not a member?",bg="#415D80",fg="White")
        member_label.config(font=("Cambria",12,"italic"))
        member_label.pack(pady=(10,0))

        register_btn=Button(self.root,text="Register",width=10,command=self.register)
        register_btn.config(font=("Cambria",10,"italic"))
        register_btn.pack(pady=(0,0))

    def register(self):

        self.clear()

        heading=Label(self.root,text="Weather Application",bg="#4158D0",fg="White")
        heading.config(font=("Cambria",24,"bold"))
        heading.pack(pady=(50,49))

        username_label=Label(self.root,text="Enter Username",bg="#4158D0",fg="white")
        username_label.config(font=("Cambria",16,"italic"))
        username_label.pack(pady=(5,5))
        self.username_input=Entry(self.root,width=25)
        self.username_input.config(font=("Cambria",16,"italic"))
        self.username_input.pack(pady=(5,10),ipady=1)

        email_label=Label(self.root,text="Enter Email",bg="#4158D0",fg="white")
        email_label.config(font=("Cambria",16,"italic"))
        email_label.pack(pady=(5,5))
        self.email_input=Entry(self.root,width=25)
        self.email_input.config(font=("Cambria",16,"italic"))
        self.email_input.pack(pady=(5,10),ipady=1)

        password_label=Label(self.root,text="Enter password",bg="#4158D0",fg="White")
        password_label.config(font=("Cambria",16,"italic"))
        password_label.pack(pady=(5,5))
        self.password_input=Entry(self.root,width=25,show="*")
        self.password_input.config(font=("Cambria",16,"italic"))
        self.password_input.pack(pady=(5,35),ipady=1)

        register_btn=Button(self.root,text="Register",width=10,command=self.perform_registration)
        register_btn.config(font=("Cambria",16,"italic"))
        register_btn.pack(pady=(5,5))

        member_label=Label(self.root,text="Already a member?",width=20)
        member_label.config(font=("Cambria",12,"italic"))
        member_label.pack(pady=(5,0))

        login_btn=Button(self.root,text="Login",width=10,command=self.login)
        login_btn.config(font=("Cambria",12,"italic"))
        login_btn.pack(pady=(10,10))

    def perform_registration(self):

        username=self.username_input.get()
        email=self.email_input.get()
        password=self.password_input.get()

        response=self.dbo.register_user(username,email,password)

        if response==0:
            messagebox.showwarning("Failed","Email alredy register")
            self.login()
        else:
            messagebox.showinfo("success","Email register")
            self.login()

    def perform_login(self):
        email=self.email_input.get()
        password=self.password_input.get()

        response=self.dbo.check_login(email,password)

        if response==1:
            messagebox.showinfo("success","Login Sucessfully")
            self.home()
        elif response==0:
            messagebox.showerror("Failed","Incorrect password")
            self.login()
        else:
            messagebox.showwarning("Failed","Email not registerd")
            self.register()

    def home(self):

        self.clear()

        heading=Label(self.root,text="Weather Application",bg="#4158D0",fg="White")
        heading.config(font=("Cambria",24,"italic","bold"))
        heading.pack(pady=(50,75))

        search_by_city_btn=Button(self.root,text="Search By City Name",width=20,height=2,command=self.using_city_name)
        search_by_city_btn.config(font=("Cambria",18,"italic"))
        search_by_city_btn.pack(pady=(5,5))

        search_by_coordinates_btn=Button(self.root,text="Search By Co-ordinates",width=20,height=2,command=self.using_coordinates)
        search_by_coordinates_btn.config(font=("Cambria",18,"italic"))
        search_by_coordinates_btn.pack(pady=(50,50))

        logout_btn=Button(self.root,text="Logout",width=10,height=1,command=self.login)
        logout_btn.config(font=("Cambria",12,"italic"))
        logout_btn.pack(pady=(25,5))

    def using_city_name(self):

        self.clear()

        heading=Label(self.root,text="Weather Application",bg="#4158D0",fg="White")
        heading.config(font=("Cambria",24,"italic","bold"))
        heading.pack(pady=(25,5))

        city_label=Label(self.root,text="Enter City Name",bg="#4158D0",fg="White")
        city_label.config(font=("cambria",16,"italic"))
        city_label.pack(pady=(5,5))

        self.city_input=Entry(self.root,width=25)
        self.city_input.config(font=("Cambria",16,"italic"))
        self.city_input.pack(pady=(5,5),ipady=1)

        search_by_city_btn=Button(self.root,text="Search",width=10,command=self.display_info)
        search_by_city_btn.config(font=("Cambria",16,"italic"))
        search_by_city_btn.pack(pady=(5,25))

        self.result=Label(self.root,text="",bg="#4158D0",fg="White")
        self.result.config(font=("Cambria",15,"italic"))
        self.result.pack(pady=(5,5))

        back_btn=Button(self.root,text="Back",width=10,command=self.login)
        back_btn.config(font=("Cambria",12,"italic"))
        back_btn.pack(pady=(5,5))

    def using_coordinates(self):

        self.clear()

        heading=Label(self.root,text="Weather Application",bg="#4158D0",fg="White")
        heading.config(font=("Cambria",24,"italic","bold"))
        heading.pack(pady=(25,5))

        lat_label=Label(self.root,text="Enter Latitude",bg="#4158D0",fg="White")
        lat_label.config(font=("Cambria",16,"italic"))
        lat_label.pack(pady=(5,5))
        lat_input=Entry(self.root,width=25)
        lat_input.config(font=("Cambria",16,"italic"))
        lat_input.pack(pady=(5,5),ipady=1)

        lon_label=Label(self.root,text="Enter Longitude",bg="#4158D0",fg="White")
        lon_label.config(font=("Cambria",16,"italic"))
        lon_label.pack(pady=(5,5))
        lon_input=Entry(self.root,width=25)
        lon_input.config(font=("Cambria",16,"italic"))
        lon_input.pack(pady=(5,5),ipady=1)

        search_by_coordinates_btn=Button(self.root,text="Search",width=10)
        search_by_coordinates_btn.config(font=("Cambria",16,"italic"))
        search_by_coordinates_btn.pack(pady=(5,5))

        back_btn=Button(self.root,text="Back",width=10,command=self.home)
        back_btn.config(font=("Cambria",12,"italic"))
        back_btn.pack(pady=(5,5))


    def display_info(self):
        city=self.city_input.get()
        data=self.apio.get_info_by_city_name(city)

        if data ==0:
            self.result["text"]="City not found"

        else:
            
            txt=""
            for i in data:
                txt +=str(i) + "->" +str(data[i]) +"\n\n"
            self.result["text"]=txt



we=weatherApplication()








