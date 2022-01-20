import tkinter
import PIL.ImageTk
from tkinter import *
from PIL import ImageTk, Image

scvalue = ""


class Calculator(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title('Calculator')
        self.geometry('350x530')
        self.logo = Image.open('logo.jpg')
        self.logo = ImageTk.PhotoImage(self.logo)
        self.wm_iconphoto(False, self.logo)
        global scvalue
        scvalue = StringVar()
        self.screen = Entry(self, textvar=scvalue, font='lucida 40 bold')
        self.screen.pack(fill=X, anchor='nw', padx=8, pady=10)
        # Frame Button
        self.f = Frame(self, bg='grey')
        self.b = Button(self.f, text='9', bg='grey', font='lucida 20 bold', padx=17, pady=1)
        self.b.pack(side=LEFT, padx=18, pady=15)
        self.b.bind("<Button-1>", self.click)
        self.b = Button(self.f, text='8', bg='grey', font='lucida 20 bold', padx=17, pady=1)
        self.b.pack(side=LEFT, padx=18, pady=15)
        self.b.bind("<Button-1>", self.click)
        self.b = Button(self.f, text='7', bg='grey', font='lucida 20 bold', padx=17, pady=1)
        self.b.pack(side=LEFT, padx=18, pady=15)
        self.b.bind("<Button-1>", self.click)
        self.f.pack()
        # Frame Button
        self.f = Frame(self, bg='grey')
        self.b = Button(self.f, text='6', bg='grey', font='lucida 20 bold', padx=17, pady=1)
        self.b.pack(side=LEFT, padx=18, pady=10)
        self.b.bind("<Button-1>", self.click)
        self.b = Button(self.f, text='5', bg='grey', font='lucida 20 bold', padx=17, pady=1)
        self.b.pack(side=LEFT, padx=18, pady=10)
        self.b.bind("<Button-1>", self.click)
        self.b = Button(self.f, text='4', bg='grey', font='lucida 20 bold', padx=17, pady=1)
        self.b.pack(side=LEFT, padx=18, pady=10)
        self.b.bind("<Button-1>", self.click)
        self.f.pack()
        # Frame Button
        self.f = Frame(self, bg='grey')
        self.b = Button(self.f, text='3', bg='grey', font='lucida 20 bold', padx=17, pady=1)
        self.b.pack(side=LEFT, padx=18, pady=10)
        self.b.bind("<Button-1>", self.click)
        self.b = Button(self.f, text='2', bg='grey', font='lucida 20 bold', padx=17, pady=1)
        self.b.pack(side=LEFT, padx=18, pady=10)
        self.b.bind("<Button-1>", self.click)
        self.b = Button(self.f, text='1', bg='grey', font='lucida 20 bold', padx=17, pady=1)
        self.b.pack(side=LEFT, padx=18, pady=10)
        self.b.bind("<Button-1>", self.click)
        self.f.pack()
        # Frame Button
        self.f = Frame(self, bg='grey')
        self.b = Button(self.f, text='0', bg='grey', font='lucida 20 bold', padx=17, pady=1)
        self.b.pack(side=LEFT, padx=18, pady=10)
        self.b.bind("<Button-1>", self.click)
        self.b = Button(self.f, text='+', bg='grey', font='lucida 20 bold', padx=17, pady=1)
        self.b.pack(side=LEFT, padx=18, pady=10)
        self.b.bind("<Button-1>", self.click)
        self.b = Button(self.f, text='-', bg='grey', font='lucida 20 bold', padx=17, pady=1)
        self.b.pack(side=LEFT, padx=18, pady=10)
        self.b.bind("<Button-1>", self.click)
        self.f.pack()
        # Frame Button
        self.f = Frame(self, bg='grey')
        self.b = Button(self.f, text='*', bg='grey', font='lucida 20 bold', padx=17, pady=1)
        self.b.pack(side=LEFT, padx=18, pady=10)
        self.b.bind("<Button-1>", self.click)
        self.b = Button(self.f, text='/', bg='grey', font='lucida 20 bold', padx=17, pady=1)
        self.b.pack(side=LEFT, padx=18, pady=10)
        self.b.bind("<Button-1>", self.click)
        self.b = Button(self.f, text='=', bg='grey', font='lucida 20 bold', padx=17, pady=1)
        self.b.pack(side=LEFT, padx=18, pady=10)
        self.b.bind("<Button-1>", self.click)
        self.f.pack()
        # Frame Button
        self.f = Frame(self, bg='grey')
        self.b = Button(self.f, text='C', bg='grey', font='lucida 20 bold', padx=17, pady=1)
        self.b.pack(side=LEFT, padx=18, pady=10)
        self.b.bind("<Button-1>", self.click)
        self.f.pack()
        self.mainloop()

    def click(self, event):
        global scvalue
        self.value = 0
        text = event.widget.cget('text')
        if text == "=":
            try:
                self.value = eval(scvalue.get())
                scvalue.set(self.value)
                self.screen.update()
            except Exception as e:
                scvalue.set('Error')
                self.screen.update()
        elif text == 'C':
            scvalue.set("")
            self.screen.update()
        else:
            scvalue.set(scvalue.get() + text)
            self.screen.update()


if __name__ == '__main__':
    cal = Calculator()
