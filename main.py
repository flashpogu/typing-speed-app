from tkinter import *
import tkinter
import random


# Setup
root = Tk()
root.title("Typing Speed Test")
root.geometry("1200x700")
root.option_add("*Label*Font", "consolas 30")
root.option_add("*Button*Font", "consolas 30")


def keyPressed(e=None):
    """ This the main function and backbone of this application"""

    try:
        if e.char.lower() == rightLabel.cget("text")[0].lower():
#           Deleting one from the right side
            rightLabel.configure(text=rightLabel.cget("text")[1:])
#           Deleting one from the left side
            leftLabel.configure(text=leftLabel.cget("text") + e.char.lower())
#           Set the next label
            currentLetterLabel.configure(text=rightLabel.cget("text")[0])
    except tkinter.TclError:
        pass

def resetWritingLabel():
    with open("words.txt") as file:
        possible_text = [line.strip() for line in file]
        text = random.choice(possible_text).lower()

    # Defining SpiltPoint
    print(text)
    print(possible_text)
    splitPoint = 0
    global rightLabel
    rightLabel = Label(root, text=text[splitPoint:])
    rightLabel.place(relx=0.5, rely=0.5, anchor=W)

    global leftLabel
    leftLabel = Label(root, text=text[0:splitPoint], fg="grey")
    leftLabel.place(relx=0.5, rely=0.5, anchor=E)
    #
    global currentLetterLabel
    currentLetterLabel = Label(root, text=text[splitPoint], fg="grey")
    currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)
    #
    global timeLeftLabel
    timeLeftLabel = Label(root, text=f"0 Seconds", fg="grey")
    timeLeftLabel.place(relx=0.5, rely=0.4, anchor=S)

    global writeAble
    writeAble = True
    root.bind("<Key>", keyPressed)
    #
    global passedSeconds
    passedSeconds = 0

    root.after(60000, stopTest)
    root.after(1000, addSeconds)


def stopTest():
    global writeAble
    writeAble = False

#   Calculating the amount of words
    amountWords = len(leftLabel.cget("text").split(" "))

#   Destroy
    timeLeftLabel.destroy()
    currentLetterLabel.destroy()
    rightLabel.destroy()
    leftLabel.destroy()

#   Display result
    global resultLabel
    resultLabel = Label(root, text=f"Words per Minute: {amountWords}", fg="black")
    resultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

#   Button Restart
    global restartButton
    restartButton = Button(root, text=f"Retry", command=restart)
    restartButton.place(relx=0.5, rely=0.6, anchor=CENTER)
def restart():

    resultLabel.destroy()
    restartButton.destroy()

    resetWritingLabel()

def addSeconds():
    global passedSeconds
    passedSeconds += 1
    timeLeftLabel.configure(text=f"{passedSeconds} Seconds")

    if writeAble:
        root.after(1000, addSeconds)



resetWritingLabel()
root.mainloop()