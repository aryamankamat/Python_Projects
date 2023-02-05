from tkinter import *
import time

root = Tk()
root.title("DIGITAL WATCH")
root.geometry("500x400")

root.config(background="black")


# root.resizable(0, 0)

# root.overrideredirect(1) #Hides the title bar of the screen or window

def Time():
    t = time.strftime("%Y-%W-%a")
    t1 = time.strftime("%H:%M:%S  %p")
    lbl0.config(text=t)
    lbl1.config(text=t1)
    lbl1.after(200, Time)


lbl0 = Label(root, font=("ds-digital", 50, "bold"), bg='black', fg="green", bd=50)
lbl1 = Label(root, font=("ds-digital", 50, "bold"), bg='black', fg="green", bd=50)

# lbl.grid(row=0,column=1)
lbl0.pack()
lbl1.pack()
Time()
print("Clock has been started...")
root.mainloop()
