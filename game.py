# resolution: 1280x720
from tkinter import Tk, Canvas, PhotoImage, Button, messagebox
import random, os

width = 1280
height = 720

def createButtons():
    global menuResume, menuStart, menuQuit, menuDelete
    menuResume = Button(window, text="Resume Game", command=resumeGame, width=15, height=2)
    menuResume.place(x=800, y=200)
    menuStart = Button(window, text="Star New Game", command=startNewGame, width=15, height=2)
    menuStart.place(x=800, y=250)
    menuDelete = Button(window, text="Delete Save File", command=deleteSave, width=15, height=2)
    menuDelete.place(x=800, y=300)
    menuQuit = Button(window, text="Quit Game", command=quitGame, width=15, height=2)
    menuQuit.place(x=800, y=350)

def resumeGame():
    if checkSaveFile():
        clearButtons()
        window.configure(bg="black")
    else:
        messagebox.showerror(title="Save File Not Found", message="Save file not exist! Please start a new game!")

def startNewGame():
    result = True
    if checkSaveFile():
        a = messagebox.askquestion(title="Save File Exist", message="There is a save file exist! If you continue to"
                                                                    " start, the file will be replaced!")
        if a == "yes":
            result = True
        elif a == "no":
            result = False
    if result:
        clearButtons()
        saveFile = open("save.dat", 'w')
        saveFile.close()
        window.configure(bg="black")

def deleteSave():
    if checkSaveFile():
        a = messagebox.askquestion(title="Confirm", message="Are you sure you want to delete save file?")
        if a == "yes":
            os.remove("save.dat")
            messagebox.showinfo(title="Done", message="Save file is deleted!")
        elif a == "no":
            messagebox.showinfo(title="Fine", message="The save file is not deleted")
    else:
        messagebox.showerror(title="Error", message="Save file not found!")


def checkSaveFile():
    dir = os.listdir()
    for file in dir:
        if file == "save.dat":
            return True
    return False

def quitGame():
    window.destroy()

def clearButtons():
    global menuResume, menuStart, menuQuit, menuDelete
    canvas.configure(bg="black")
    for thisButton in buttonList:
        thisButton.destroy()

def setWindowDimensions(w, h):
    global middleX, middleY
    window = Tk()
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    middleX = (ws/2) - (w/2)
    middleY = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, middleX, middleY))
    return window

def destroyBKI():
    global BKI
    BKI.destroy()

def bossKey(event):     #Press Control+b to use boss key, click the image to go back
    global bossKeyImage, BKI
    BKI = Button(window, image=bossKeyImage, width="1280", height="720", command=destroyBKI)
    BKI.place(x=0, y=0)

window = setWindowDimensions(width, height)
canvas = Canvas(window, bg="#66CCFF", width=width, height=height)
window.title("Game Test")
bossKeyImage = PhotoImage(file="bossKeyImage.png")
createButtons()
buttonList = [menuQuit, menuStart, menuResume, menuDelete]
canvas.bind("<Control-b>", bossKey)
canvas.focus_set()
canvas.pack()
window.mainloop()