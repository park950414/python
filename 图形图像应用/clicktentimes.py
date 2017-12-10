from graphics import *
def main():
    win = GraphWin("Click Me!")
    for i in range(10):
        p = win.getMouse() #程序暂停等待指令
        print("You clicked at:",p.getX(),p.getY())

if __name__ == '__main__':
    print("Please click anywhere")
    main()
