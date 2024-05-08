from tkinter import *
import random

def tura_urmatoare(row,column):
    global jucatori
    global jucator
    if butoane[row][column]["text"] == "" and castigator() is False:
        if jucator == jucatori[0]:
            butoane[row][column]["text"] =jucator

            if castigator() is False:
                jucator = jucatori[1]
                tabel.config(text =("tura lui: " + jucatori[1]))

            elif castigator() is True:

                tabel.config(text=("castiga "+ jucatori[0]) )

            elif castigator() == "egalitate":
                tabel.config(text= ("egalitate"))
        else:
            butoane[row][column]["text"] = jucator

            if castigator() is False:
                jucator = jucatori[0]
                tabel.config(text=("tura lui: " + jucatori[0]))

            elif castigator() is True:

                tabel.config(text=("castiga " + jucatori[1]))

            elif castigator() == "egalitate":
                tabel.config(text=("egalitate"))




def castigator():
    for row in range(3):
        if butoane[row][0]['text'] == butoane[row][1]['text'] == butoane[row][2]['text'] != "":
            butoane[row][0].config(bg="green")
            butoane[row][1].config(bg="green")
            butoane[row][2].config(bg="green")
            return True

    for column in range(3):
        if butoane[0][column]['text'] == butoane[1][column]['text'] == butoane[2][column]['text'] != "":
            butoane[0][column].config(bg="green")
            butoane[1][column].config(bg="green")
            butoane[2][column].config(bg="green")
            return True

    if butoane[0][0]['text'] == butoane[1][1]['text'] == butoane[2][2]['text'] != "":
        butoane[0][0].config(bg="green")
        butoane[1][1].config(bg="green")
        butoane[2][2].config(bg="green")
        return True

    elif butoane[0][2]['text'] == butoane[1][1]['text'] == butoane[2][0]['text'] != "":
        butoane[0][2].config(bg="green")
        butoane[1][1].config(bg="green")
        butoane[2][0].config(bg="green")
        return True

    elif spatii_goale() is False:

        for row in range(3):
            for column in range(3):
                butoane[row][column].config(bg="yellow")
        return "egalitate"

    else:
        return False



def spatii_goale():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if butoane[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True
    

def joc_nou():
    global jucator


    jucator = random.choice(jucatori)

    tabel.config(text=jucator + " turn")

    for row in range(3):
        for column in range(3):
            butoane[row][column].config(text="", bg="#F0F0F0")


window = Tk()
window.title("X si 0")
jucatori = ["x", "0"]
jucator = random.choice(jucatori)

butoane = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]


tabel = Label(text="tura lui: " + jucator, font=("consolas", 30))
tabel.pack(side="top")

resetare = Button(text="reset", font=("consolas", 15), command=joc_nou)
resetare.pack(side="bottom")

rama = Frame(window)
rama.pack()

for row in range(3):
    for column in range(3):
        butoane[row][column] = Button(rama, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: tura_urmatoare(row,column))
        butoane[row][column].grid(row=row,column=column)



window.mainloop()
