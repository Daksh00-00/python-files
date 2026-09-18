import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk

#window
window=ttk.Window(themename="minty")

window.geometry("900x600")
window.config(background="#E8EDD0")
window.title("Green care")

#image ig
og_image=Image.open("background.jpg")


#canvas
canvas=ttk.Canvas(master=window,highlightthickness=0)
canvas.pack(fill="both",expand=True)

#resize the f-ing background 
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
                 background="#E8EDD0")

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
                     background="#E8EDD0",
                     foreground="green")
title_label.pack(pady=30,padx=10)

#welcome
welcome_label=ttk.Label(master=frame1,
                        text="Welcome",
                        font=("roboto",20,"bold"),
                        background="#E8EDD0",
                        foreground="green")
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
                        bootstyle="success",
                        command= lambda:open_login("Admin"))
admin_button.pack(pady=20)

client_button=ttk.Button(master=frame2,
                         text="Client",
                         width=20,bootstyle="success",
                         command= lambda:open_login("Client"))
client_button.pack(pady=20)

##
frame2.pack(pady=25)

##
main_frame.place(relx=0.5,rely=0.5,anchor="center")

#admin and client and whoever  login thingy
def open_login(user_type):
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
    background="#E8EDD0",
    foreground="green")
login_title.pack(pady=30)

#username
username_label = ttk.Label(
    master=login_frame,
    text="Username",
    font=("Segoe UI", 12, "bold"),
    background="#E8EDD0",
    foreground="green")
username_label.pack()

username_entry = ttk.Entry(
    master=login_frame,
    width=30)
username_entry.pack(pady=5,padx=50)

#password
password_label = ttk.Label(
    master=login_frame,
    text="Password",
    font=("Segoe UI", 12, "bold"),
    background="#E8EDD0",
    foreground="green")
password_label.pack(pady=(15, 0))

password_entry = ttk.Entry(
    master=login_frame,
    width=30,
    show="*")
password_entry.pack(pady=5,padx=50)

#login button
login_button = ttk.Button(
    master=login_frame,
    text="Login",
    width=20,
    bootstyle="success")
login_button.pack(pady=20)

# register button
register_button = ttk.Button(
    master=login_frame,
    text="Register",
    width=20,
    bootstyle="outline-success")
register_button.pack()

#back button
back_button = ttk.Button(
    master=login_frame,
    text="← Back",
    bootstyle="link-success",command=back_ig)
back_button.pack(pady=15)


#mainloop
window.mainloop()