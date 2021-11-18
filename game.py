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


def moveCharacter():
    global character, direction
    positions = []
    positions.append(canvas.coords(character))
    if positions[0][0] < 0:
        canvas.coords(character, width, positions[0][1], width - characterSize, positions[0][3])
    elif positions[0][2] > width:
        canvas.coords(character, 0 - characterSize, positions[0][1], 0, positions[0][3])
    elif positions[0][3] > height:
        canvas.coords(character, positions[0][0], 0 - characterSize, positions[0][2], 0)
    elif positions[0][1] < 0:
        canvas.coords(character, positions[0][0], height, positions[0][2], height - characterSize)
    positions.clear()
    if direction == "left":
        canvas.move(character, -characterSize, 0)
    elif direction == "right":
        canvas.move(character, characterSize, 0)
    elif direction == "up":
        canvas.move(character, 0, -characterSize)
    elif direction == "down":
        canvas.move(character, 0, characterSize)


def resumeGame():
    global character
    if checkSaveFile():
        clearButtons()
        score = 0
        txt = "Score:" + str(score)
        scoreText = canvas.create_text(width / 2, 20, fill="white", font="Times 20 italic bold", text=txt)
        character = canvas.create_rectangle(characterSize, characterSize, characterSize * 2, characterSize * 2,
                                            fill="blue")
        moveCharacter()
    else:
        messagebox.showerror(title="Save File Not Found", message="Save file not exist! Please start a new game!")

def leftKey(event):
    global direction, pause
    direction = "left"
    pause = False
    moveCharacter()

def rightKey(event):
    global direction, pause
    direction = "right"
    pause = False
    moveCharacter()

def upKey(event):
    global direction, pause
    direction = "up"
    pause = False
    moveCharacter()

def downKey(event):
    global direction, pause
    direction = "down"
    pause = False
    moveCharacter()

def pauseKey(event):
    global direction, pause
    direction = "pause"
    pause = True

def startNewGame():
    global character
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
        score = 0
        txt = "Score:" + str(score)
        scoreText = canvas.create_text(width / 2, 20, fill="white", font="Times 20 italic bold", text=txt)
        character = canvas.create_rectangle(characterSize, characterSize, characterSize * 2, characterSize * 2,
                                            fill="blue")
        moveCharacter()


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
    canvas.configure(bg="black")
    for thisButton in buttonList:
        thisButton.destroy()


def setWindowDimensions(w, h):
    window = Tk()
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    middleX = (ws / 2) - (w / 2)
    middleY = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, middleX, middleY))
    return window


def destroyBKI():
    global BKI
    BKI.destroy()


def bossKey(event):  # Press Control+b to use boss key, click the image to go back
    global bossKeyImage, BKI
    BKI = Button(window, image=bossKeyImage, width="1280", height="720", command=destroyBKI)
    BKI.place(x=0, y=0)


window = setWindowDimensions(width, height)
canvas = Canvas(window, bg="#66CCFF", width=width, height=height)
window.title("Game Test")
bossKeyImage = PhotoImage(file="bossKeyImage.png")
createButtons()
characterSize = 15
buttonList = [menuQuit, menuStart, menuResume, menuDelete]
direction = "down"
canvas.bind("<Control-b>", bossKey)
canvas.bind("<Left>", leftKey)
canvas.bind("<Right>", rightKey)
canvas.bind("<Up>", upKey)
canvas.bind("<Down>", downKey)
canvas.bind('<Key-p>', pauseKey)
canvas.focus_set()
canvas.pack()
window.mainloop()
