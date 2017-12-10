from tkinter import *

def processOK():
    print("OK button in clicked")

def processCancel():
    print("Cancel button is clicked")

def main():
    tk = Tk()
    btnOK = Button(tk,text = 'OK',fg = 'red', command = processOK)
    btnCancel = Button(tk,text = 'Cancel',bg = 'yellow', command = processCancel)
    btnOK.pack()
    btnCancel.pack()
    tk.mainloop()

main()
