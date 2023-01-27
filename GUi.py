from tkinter import *

class GUITest(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
    def setupGUI(self):
        Label1 = Label(self.master, text="A label")
        Label1.grid(row=0, column=0, sticky=W)

        Label2 = Label(self.master, text="Another Label")
        Label2.grid(row=1, column=0, sticky=W)

        Label3 = Label(self.master, text="A third label, centered")
        Label3.grid(row=2, column=0, columnspan=2, sticky=E+W)

        img = PhotoImage(file="Hair needs cut.png")
        Label4 = Label(self.master, image=img)
        Label4.image = img
        Label4.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=N+S+E+W)

window = Tk()
t = GUITest(window)
t.setupGUI()
window.mainloop()