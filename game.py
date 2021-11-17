# resolution: 1280x720
from tkinter import Tk, Canvas, PhotoImage, Button
import random

width = 1280
height = 720


def quitGame():
    window.destroy()


def setWindowDimensions(w, h):
    global middleX, middleY
    window = Tk()
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    middleX = (ws/2) - (w/2)
    middleY = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, middleX, middleY))
    return window


window = setWindowDimensions(width, height)
canvas = Canvas(window, bg="#66CCFF", width=width, height=height)
window.title("Game Test")
menuResume = Button(window, text="Resume Game", command=None, width=15, height=2)
menuResume.place(x=800, y=200)
menuResume = Button(window, text="Star New Game", command=None, width=15, height=2)
menuResume.place(x=800, y=250)
menuResume = Button(window, text="Quit Game", command=quitGame, width=15, height=2)
menuResume.place(x=800, y=300)
canvas.pack()
window.mainloop()