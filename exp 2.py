import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

#function
def convert():
    mile_input=entry_int.get()

    km_output= mile_input * 1.61
    km_output=round(km_output,5)
    output_string.set(str(km_output)+" km")


#window
window=ttk.Window(themename ="darkly")
window.title("unit coverter")
window.geometry("350x200")

#title
title_label = ttk.Label(master = window,text="Miles to kilometers"
                        , font="calibri 24 bold")
title_label.pack()

#input 
input_frame = ttk.Frame(master = window)

entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame
                  ,textvariable = entry_int)
button =ttk.Button(master= input_frame,text="convert"
                   ,command=convert)

entry.pack(side ="left",padx=10)
button.pack(side ="left")
input_frame.pack(pady =10)



#packing the button and entry into input frame
#then packing input frame into windows

#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window,text ="output"
                         ,font="calibri 24"
                         ,textvariable = output_string)
output_label.pack()



#run
window.mainloop()