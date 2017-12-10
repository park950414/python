from tkinter import *

tk = Tk()
canvas = Canvas(tk,width = 400,height = 400)
canvas.pack()

def moverectangle(event):
    if event.keysym == "Up":
        canvas.move(1,0,-5)
    elif event.keysym == "Down":
        canvas.move(1,0,5)
    elif event.keysym == "Left":
        canvas.move(1,-5,0)
    elif event.keysym == "Right":
        canvas.move(1,5,0)

canvas.create_rectangle(10,10,50,50,fill="red")
canvas.bind_all("<KeyPress-Up>",moverectangle)
canvas.bind_all("<KeyPress-Down>",moverectangle)
canvas.bind_all("<KeyPress-Left>",moverectangle)
canvas.bind_all("<KeyPress-Right>",moverectangle)
