from tkinter import *

tk =Tk()
canvas = Canvas(tk,width = 200, height = 200)
canvas.pack()
canvas.create_text(100,40,text = "Welcome to Tkinter",fill = 'blue',font =\
                   ("TIMES",16))
myImage = PhotoImage(file = "soccerdog.gif")
canvas.create_image(10,70,anchor = NW,image = myImage)
canvas.create_rectangle(10,70,190,130)

tk.mainloop()
