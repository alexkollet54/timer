from tkinter import *
import time


def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000,update_time)

root = Tk()
root.title("Clock")
root.geometry("500x250")

time_label = Label(root, font=("Arial",80), bg="white", fg="black")
time_label.pack(pady=50)

update_time()




root.mainloop()