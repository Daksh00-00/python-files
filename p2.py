import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from tkinter import messagebox


#window
window=ttk.Window(themename="minty")

window.geometry("900x600")
window.config(background="#F3F6EA")
window.title("Green care")

#image ig
og_image=Image.open("back.png")


#canvas
canvas=ttk.Canvas(master=window,highlightthickness=0)
canvas.pack(fill="both",expand=True)

#resize the background 
def back_ground(event):
    new_image=og_image.resize((event.width,event.height))
    new_image=ImageTk.PhotoImage(new_image)

    canvas.itemconfig(background,image=new_image)
    canvas.image=new_image
background=canvas.create_image(0,0,
                               image=ImageTk.PhotoImage(og_image),
                               anchor="nw")

canvas.bind("<Configure>",back_ground)


#frame style
style = ttk.Style()
style.configure("Green.TFrame",
                 background="#F3F6EA")

#button style
style.configure("Zap.TButton",
                 background="#215A17",
                 foreground="#C1DAC3",
                 bordercolor="#21471A")

style.map("Zap.TButton",
          background=[("active", "#25561B")],
          foreground=[("active", "#FFFFFF")])

#main frame
main_frame=ttk.Frame(master=window,
                     style="Green.TFrame",
                     width=400,height=400)

#title frame 
frame1=ttk.Frame(master=main_frame,
                 style="Green.TFrame")

#title
title_label=ttk.Label(master=frame1,
                      text="Green Care",
                     font=("Segoe UI",25,"bold"),
                     background="#F3F6EA",
                     foreground="#2F5D50")
title_label.pack(pady=30,padx=10)

#welcome
welcome_label=ttk.Label(master=frame1,
                        text="Welcome",
                        font=("roboto",20,"bold"),
                        background="#F3F6EA",
                        foreground="#2F5D50")
welcome_label.pack(pady=20)

##
frame1.pack()

#button frame 
frame2=ttk.Frame(master=main_frame,
                 style="Green.TFrame")

#button
admin_button=ttk.Button(master=frame2,
                        text="Admin",
                        width=20,
                        style="Zap.TButton",
                        command= lambda:open_login("Admin"))
admin_button.pack(pady=20)

client_button=ttk.Button(master=frame2,
                         text="Client",
                         width=20,style="Zap.TButton",
                         command= lambda:open_login("Client"))
client_button.pack(pady=20)

##
frame2.pack(pady=25)

##
main_frame.place(relx=0.5,rely=0.5,anchor="center")

#admin and client and whoever  login thingy

current_user=""

def open_login(user_type):

    global current_user

    current_user=user_type
    
    main_frame.place_forget()

    login_title.config(text=user_type + " Login")

    login_frame.place(relx=0.5, rely=0.5, anchor="center")

def back_ig():
    login_frame.place_forget()
    main_frame.place(relx=0.5,rely=0.5,anchor="center")


#login frame
login_frame = ttk.Frame(
    master=window,
    style="Green.TFrame",
    width=400,
    height=400)

#login title
login_title = ttk.Label(
    master=login_frame,
    text="Admin Login",
    font=("Segoe UI", 25, "bold"),
    background="#F3F6EA",
    foreground="#2F5D50")
login_title.pack(pady=30)

#username
username_label = ttk.Label(
    master=login_frame,
    text="Username",
    font=("Segoe UI", 12, "bold"),
    background="#F3F6EA",
    foreground="#2F5D50")
username_label.pack()


login_user_var=ttk.StringVar()


username_entry = ttk.Entry(master=login_frame,
                            width=30,
                            textvariable=login_user_var)
username_entry.pack(pady=5,padx=50)

#password
password_label = ttk.Label(master=login_frame,
                            text="Password",
                            font=("Segoe UI", 12, "bold"),
                            background="#F3F6EA",
                            foreground="#2F5D50")
password_label.pack(pady=(15, 0))


login_pass_var=ttk.StringVar()

password_entry = ttk.Entry(
    master=login_frame,
    width=30,
    show="*",
    textvariable=login_pass_var)
password_entry.pack(pady=5,padx=50)

#login button
login_button = ttk.Button(
    master=login_frame,
    text="Login",
    width=20,
    style="Zap.TButton",command=lambda:login_user())
login_button.pack(pady=20)

#register
def register():
    login_frame.place_forget()

    regi_title.config(text=current_user + " account")

    #Show pass key only for Admin
    if current_user == "Admin":
        regi_key.pack(pady=(15, 0))
        pass_key_entry.pack(pady=20)
    else:
        regi_key.pack_forget()
        pass_key_entry.pack_forget()



    regi_frame.place(relx=0.5, rely=0.5, anchor="center")

# register button
register_button = ttk.Button(
    master=login_frame,
    text="Register",
    width=20,
    style="Zap.TButton",command=lambda:register())
register_button.pack()

#back button
back_button = ttk.Button(
    master=login_frame,
    text="← Back",
    bootstyle="link-success",command=back_ig)
back_button.pack(pady=15)

#registreing function
def create_account():

    username=regi_username_var.get()
    password=regi_pass_var.get()
    con_password=regi_passcon_var.get()


    if username=="" or password=="" or con_password=="":
        messagebox.showwarning("Missing Informaion","Please fill all the fields")
        return

    if password != con_password:
        messagebox.showerror("Password error","Passwords do not match")
        return 

    
    result = create_user(username,
                        password,
                        current_user)

    if result:
        messagebox.showinfo("Success",
                            "Account created successfully!")

#login function (og)


def login_user():

    username=login_user_var.get().strip()

    password=login_pass_var.get()

    if username=="" or password=="":
        messagebox.showwarning("Missing information!",
                               "PLease enter both username and password")
        return
    result=check_login(username,password,current_user)

    if result:
        login_frame.place_forget()

        if current_user=="Admin":
            open_admin_window(username)


        elif current_user=="Client":
            open_client_window(username)
    else:
        messagebox.showerror("Login failed!","Incorrect username or password")



#register frame

regi_frame=ttk.Frame(master=window,
    style="Green.TFrame",
    width=400,
    height=500)

#reistre title
regi_title = ttk.Label(
    master=regi_frame,
    text="Register",
    font=("Segoe UI", 25, "bold"),
    background="#F3F6EA",
    foreground="#2F5D50")
regi_title.pack(pady=30)

#register username
regi_username_label = ttk.Label(
    master=regi_frame,
    text="Username",
    font=("Segoe UI", 12, "bold"),
    background="#F3F6EA",
    foreground="#2F5D50")
regi_username_label.pack()


regi_username_var=ttk.StringVar()

regi_username_entry = ttk.Entry(
    master=regi_frame,
    width=30, textvariable=regi_username_var)
regi_username_entry.pack(pady=5,padx=50)

#registering password
regi_password_label1 = ttk.Label(
    master=regi_frame,
    text="Password",
    font=("Segoe UI", 12, "bold"),
    background="#F3F6EA",
    foreground="#2F5D50")
regi_password_label1.pack(pady=(15, 0))

regi_pass_var=ttk.StringVar()

regi_password_entry1 = ttk.Entry(
    master=regi_frame,
    width=30,
    show="*",
    textvariable=regi_pass_var)
regi_password_entry1.pack(pady=5,padx=50)

#pass confirmation

regi_passcon_var=ttk.StringVar()

regi_password_label2 = ttk.Label(
    master=regi_frame,
    text="Confirm Password",
    font=("Segoe UI", 12, "bold"),
    background="#F3F6EA",
    foreground="#2F5D50")
regi_password_label2.pack(pady=(15, 0))

regi_password_entry2 = ttk.Entry(
    master=regi_frame,
    width=30,
    show="*",textvariable=regi_passcon_var)
regi_password_entry2.pack(pady=5,padx=50)

#pass key 
regi_key = ttk.Label(
        master=regi_frame,
        text="Pass Key",
        font=("Segoe UI", 12, "bold"),
        background="#F3F6EA",
        foreground="#2F5D50")
regi_key.pack(pady=(15, 0))


#pass key for admin

pass_key=ttk.StringVar()


pass_key_entry=ttk.Entry( master=regi_frame,
width=30, textvariable=pass_key)
pass_key_entry.pack(pady=20)


#create account
create_button = ttk.Button(
    master=regi_frame,
    text="Create Account",
    width=20,
    style="Zap.TButton",
    command=create_account)
create_button.pack(pady=20)


#registration back button ,the function
def register_back():

    regi_frame.place_forget()

    login_frame.place(
        relx=0.5,
        rely=0.5,
        anchor="center")


#registration back button 
regi_back_button = ttk.Button(
    master=regi_frame,
    text="← Back",
    bootstyle="link-success",
    command=lambda: register_back())

regi_back_button.pack(pady=20)



def logout(current_window):
    current_window.destroy()
    window.deiconify()


def open_admin_window(username):

    window.withdraw()

    admin_window = tk.Toplevel(window)

    admin_window.geometry("1000x650")

    admin_window.title("Green Care - Admin")

    admin_window.config(background="#F3F6EA")

    title = ttk.Label(
        admin_window,
        text=f"Welcome Admin, {username}",
        font=("Segoe UI", 24, "bold"),
        background="#F3F6EA",
        foreground="#2F5D50")

    title.pack(pady=40)

    logout_button = ttk.Button(
        admin_window,
        text="Logout",
        style="Zap.TButton",
        command=lambda:logout(admin_window))

    logout_button.pack()
        

def open_client_window(username):

        window.withdraw()

        client_window = tk.Toplevel(window)

        client_window.geometry("1000x650")

        client_window.title(
        "Green Care - Client")

        client_window.config(
            background="#F3F6EA")

        title = ttk.Label(
            client_window,
            text=f"Welcome, {username}",
            font=("Segoe UI", 24, "bold"),
            background="#F3F6EA",
            foreground="#2F5D50")

        title.pack(pady=40)
        logout_button = ttk.Button(
            client_window,
            text="Logout",
            style="Zap.TButton",
            command=lambda:logout(client_window))

        logout_button.pack()

admin_frame=ttk.Frame()


#mainloop
window.mainloop()