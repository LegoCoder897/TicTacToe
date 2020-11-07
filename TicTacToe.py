from tkinter import *
from tkinter import messagebox
xoro = 'X'
Xspots = []
Ospots = []
totalx = 0



def xwins():
    print('X WINS!!!')
    messagebox.showinfo('WINNER', 'X WINS')
    clear()


def owins():
    print('O WINS!!!')
    messagebox.showinfo('WINNER', 'O WINS')
    clear()

def tie():
    messagebox.showinfo('WINNER', 'ITS A TIE')
    clear()


root = Tk()
root.configure(background='white')
root.title('Tic Tac Toe')
root.wm_resizable(height=True, width=True)



def fill(a, b):
    global button1, xoro, Ospots, Xspots, totalx
    button1 = Button(root, text=xoro, fg='black', bg='white', height=1, width=2)
    button1.grid(row=a, column=b)
    if xoro == 'X':
        xoro = 'O'
        totalx = totalx + 1
        Xspots = Xspots + [a*10 + b]
        if 11 in Xspots and 12 in Xspots and 13 in Xspots:
            xwins()
        else:
            if 21 in Xspots and 22 in Xspots and 23 in Xspots:
                xwins()
            else:
                if 31 in Xspots and 32 in Xspots and 33 in Xspots:
                    xwins()
                else:
                    if 11 in Xspots and 22 in Xspots and 33 in Xspots:
                        xwins()
                    else:
                        if 13 in Xspots and 22 in Xspots and 31 in Xspots:
                            xwins()
                        else:
                            if 11 in Xspots and 21 in Xspots and 31 in Xspots:
                                xwins()
                            else:
                                if 12 in Xspots and 22 in Xspots and 32 in Xspots:
                                    xwins()
                                else:
                                    if 13 in Xspots and 23 in Xspots and 33 in Xspots:
                                        xwins()

                                    else:
                                        if totalx == 5:
                                            tie()

    else:
        xoro = 'X'
        Ospots = Ospots + [a * 10 + b]
        if 11 in Ospots and 12 in Ospots and 13 in Ospots:
            owins()
        else:
            if 21 in Ospots and 22 in Ospots and 23 in Ospots:
                owins()
            else:
                if 31 in Ospots and 32 in Ospots and 33 in Ospots:
                    owins()
                else:
                    if 11 in Ospots and 22 in Ospots and 33 in Ospots:
                        owins()
                    else:
                        if 13 in Ospots and 22 in Ospots and 31 in Ospots:
                            owins()
                        else:
                            if 11 in Ospots and 21 in Ospots and 31 in Ospots:
                                owins()
                            else:
                                if 12 in Ospots and 22 in Ospots and 32 in Ospots:
                                    owins()
                                else:
                                    if 13 in Ospots and 23 in Ospots and 33 in Ospots:
                                        owins()


def clear():
    global Xspots, Ospots, xoro, totalx
    button11 = Button(root, text='', fg='black', bg='white', command=lambda: fill(1, 1), height=4, width=8)
    button11.grid(row=1, column=1)

    button12 = Button(root, text='', fg='black', bg='white', command=lambda: fill(1, 2), height=4, width=8)
    button12.grid(row=1, column=2)

    button13 = Button(root, text='', fg='black', bg='white', command=lambda: fill(1, 3), height=4, width=8)
    button13.grid(row=1, column=3)

    button21 = Button(root, text='', fg='black', bg='white', command=lambda: fill(2, 1), height=4, width=8)
    button21.grid(row=2, column=1)

    button22 = Button(root, text='', fg='black', bg='white', command=lambda: fill(2, 2), height=4, width=8)
    button22.grid(row=2, column=2)

    button23 = Button(root, text='', fg='black', bg='white', command=lambda: fill(2, 3), height=4, width=8)
    button23.grid(row=2, column=3)

    button31 = Button(root, text='', fg='black', bg='white', command=lambda: fill(3, 1), height=4, width=8)
    button31.grid(row=3, column=1)

    button32 = Button(root, text='', fg='black', bg='white', command=lambda: fill(3, 2), height=4, width=8)
    button32.grid(row=3, column=2)

    button33 = Button(root, text='', fg='black', bg='white', command=lambda: fill(3, 3), height=4, width=8)
    button33.grid(row=3, column=3)

    xoro = 'X'
    Xspots = []
    Ospots = []
    totalx = 0
    root.mainloop()

clear()

