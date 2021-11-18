# resolution: 1280x720
from tkinter import Tk, Canvas, PhotoImage, Button, messagebox
import random, os

width = 1280
height = 720

def placeZombie():
    global zombie, zombieSpeed
    zombie.append(canvas.create_rectangle(0, 0, characterSize, characterSize, fill="red"))
    zombieX = random.randint(0, width - characterSize)
    zombieY = random.randint(0, height - characterSize)
    canvas.move(zombie[len(zombie)-1], zombieX, zombieY)
    zombieSpeed = 300
    moveZombie()

def moveZombie():
    global zombie, character, pause, zombieSpeed, atMenu
    if not pause:
        for thisZombie in zombie:
            try:
                if canvas.coords(thisZombie)[0] < canvas.coords(character)[0]:
                    x = 10
                else:
                    x = -10
                if canvas.coords(thisZombie)[1] < canvas.coords(character)[1]:
                    y = 10
                else:
                    y = -10
                canvas.move(thisZombie, x, y)
            except IndexError:
                a = 0
    window.after(zombieSpeed, moveZombie)

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
    global character, score, scoreText, pause, txt, atMenu
    if checkSaveFile():
        clearButtons()
        score = 0
        saveFile = open('save.dat', 'r')
        readLine = saveFile.read()
        saveFile.close()
        pointer = 0
        char = 's'
        while char != '/':
            char = readLine[pointer]
            pointer += 1
        endPointer = pointer-1
        score = int(readLine[0:endPointer])
        char = 's'
        startPointer = pointer
        while char != '/':
            char = readLine[pointer]
            pointer += 1
        endPointer = pointer-1
        result = readLine[startPointer:endPointer]
        numOfZombie = int(result)
        txt = "Score:" + str(score)
        scoreText = canvas.create_text(width / 2, 20, fill="white", font="Times 20 italic bold", text=txt)
        character = canvas.create_rectangle(characterSize, characterSize, characterSize * 2, characterSize * 2,
                                            fill="blue")
        pause = False
        atMenu = False
        for i in range(numOfZombie):
            placeZombie()
        scoreIncrease()
        moveCharacter()
    else:
        messagebox.showerror(title="Save File Not Found", message="Save file not exist! Please start a new game!")

def leftKey(event):
    global direction, pause, pauseText
    direction = "left"
    pause = False
    try:
        canvas.delete(pauseText)
    except NameError:
        a = 0
    moveCharacter()

def rightKey(event):
    global direction, pause, pauseText
    direction = "right"
    pause = False
    try:
        canvas.delete(pauseText)
    except NameError:
        a = 0
    moveCharacter()

def upKey(event):
    global direction, pause, pauseText
    direction = "up"
    pause = False
    try:
        canvas.delete(pauseText)
    except NameError:
        a = 0
    moveCharacter()

def downKey(event):
    global direction, pause, pauseText
    direction = "down"
    pause = False
    try:
        canvas.delete(pauseText)
    except NameError:
        a = 0
    moveCharacter()

def pauseKey(event):
    global direction, pause, pauseText
    direction = "pause"
    pause = True
    pauseText = canvas.create_text(width/2, height/2, fill="white", font="Times 50 bold", text="PAUSE")

def save(event):
    global score
    saveFile = open("save.dat", 'w')
    saveFile.write(str(score))
    saveFile.write('/')
    saveFile.write(str(len(zombie)))
    saveFile.write('/')
    saveFile.close()

def startNewGame():
    global character, score, scoreText, pause, txt, atMenu
    result = True
    if checkSaveFile():
        a = messagebox.askquestion(title="Save File Exist", message="There is a save file exist! If you continue to"
                                                                    " start, the file will be replaced!")
        if a == "yes":
            result = True
        elif a == "no":
            result = False
    if result:
        atMenu = False
        clearButtons()
        saveFile = open("save.dat", 'w')
        saveFile.close()
        score = 0
        txt = "Score:" + str(score)
        scoreText = canvas.create_text(width / 2, 20, fill="white", font="Times 20 italic bold", text=txt)
        character = canvas.create_rectangle(characterSize, characterSize, characterSize * 2, characterSize * 2,
                                            fill="blue")
        pause = False
        placeZombie()
        scoreIncrease()
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

def scoreIncrease():
    global score, pause, scoreText, zombieSpeed
    if not pause:
        score += 10
        if (zombieSpeed > 200) and (score % 50 == 0) and (score != 0):
            zombieSpeed -= 25
        if score % 100 == 0:
            placeZombie()
    txt = "Score:" + str(score)
    canvas.itemconfigure(scoreText, text=txt)
    window.after(1000, scoreIncrease)

def quitGame():
    window.destroy()

def backToMenu(event):
    global character, scoreText, atMenu
    save(event)
    atMenu = True
    canvas.delete('all')
    canvas.configure(bg='#66CCFF')
    createButtons()

def clearButtons():
    global menuQuit, menuStart, menuDelete, menuResume
    canvas.configure(bg="black")
    menuQuit.destroy()
    menuStart.destroy()
    menuDelete.destroy()
    menuResume.destroy()

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


atMenu = True
window = setWindowDimensions(width, height)
canvas = Canvas(window, bg="#66CCFF", width=width, height=height)
window.title("Game Test")
bossKeyImage = PhotoImage(file="bossKeyImage.png")
createButtons()
characterSize = 15
zombie = []
direction = "down"
canvas.bind("<Control-b>", bossKey)
canvas.bind("<Left>", leftKey)
canvas.bind("<Right>", rightKey)
canvas.bind("<Up>", upKey)
canvas.bind("<Down>", downKey)
canvas.bind('<Key-p>', pauseKey)    # press p to pause, press any direction key to continue
canvas.bind('<Control-s>', save)    # press control+s to save
canvas.bind('<Control-t>', backToMenu)  # press control+t to back to menu
canvas.focus_set()
canvas.pack()
window.mainloop()
