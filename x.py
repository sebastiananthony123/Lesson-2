from tkinter import *

#Creating a window

win = Tk()

win.geometry('425x500')

win.title('Lets Make it Work!!')

win.config(bg = '#333333')

#Creating widgets

for i in range(4):
    for j in range(4):
        l1 = Label(win, bg = 'cornflowerblue', fg = 'black')
        l1.grid(padx = 10, pady = 10, ipadx = 40, ipady = 40, row = i, column = j) #ipad is internal padding


mainloop()