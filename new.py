from tkinter import *

root = Tk()
root.geometry('500x500')


def click(event):
    print("click"+str(event.x))


widget = Button(root, text='click')
widget.pack()
widget.bind('<Button-1>', click)
root.mainloop()
