from tkinter import *
from tkinter import messagebox
import time


root = Tk()

#Timer
root.title("Timer")

#Window Dimension
root.geometry("700x350")

#declartion of variables
hour= StringVar()
minute= StringVar()
second= StringVar()

#set variables to 0
hour.set("00")
minute.set("00")
second.set("00")


#use of entry class to take input
hourEntry = Entry(root, width=3, font=("Arial",18,""),
                  textvariable=hour)
hourEntry.place(x=290,y=150)

minuteEntry = Entry(root, width=3, font=("Arial",18,""),
                  textvariable=minute)
minuteEntry.place(x=340,y=150)

secondEntry = Entry(root, width=3, font=("Arial",18,""),
                  textvariable=second)
secondEntry.place(x=390,y=150)

def submit():
    try:
        #store the input in temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
        
        mins,secs = divmod(temp,60)
        
        #convert the input entered in mins or secs to hours,
        
        hours=0
        if mins >60:
            
            hours, mins = divmod(mins,60)
        
        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        
        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)
        
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
         
        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1
 
# button widget
btn = Button(root, text='Set Time Countdown', bd='5',
             command= submit)
btn.place(x = 300,y = 195)
  







root.mainloop()