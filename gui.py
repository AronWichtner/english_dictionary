from tkinter import *
import json
from difflib import get_close_matches
from KeyInput import *
import time

def execute_gui():
    data = json.load(open("data.json"))

    window = Tk()
    window.title("English_Dictionary")
    window.configure(bg="black")

    def processdata():
        keyinput = KeyInput()
        keyinput.word = word_ent.get()
        if keyinput.word == "\end":
            definition_txt.delete("1.0", END)
            definition_txt.insert(END, "Thanks for using this program!\n")
            #window.destroy()
        elif keyinput.word.lower() in data:
            keyinput.word = keyinput.word.lower()
            keyinput.status = True
        elif keyinput.word.capitalize() in data:
            keyinput.word = keyinput.word.capitalize()
            keyinput.status = True
        elif keyinput.word.upper() in data:
            keyinput.word = keyinput.word.upper()
            keyinput.status = True
        else:
            keyinput.status = False

        if keyinput.status == True:
            keyinput.definition = data[keyinput.word]
            definition_txt.delete("1.0", END)
            definition_txt.insert(END, keyinput.build_definition())
        elif len(get_close_matches(keyinput.word, data.keys())) > 0:
            close_match = get_close_matches(keyinput.word, data.keys())[0]
            keyinput.definition = data[close_match]
            definition_txt.delete("1.0", END)
            definition_txt.insert(END, "?{}?\n".format(close_match) + keyinput.build_definition())
        else:
            definition_txt.delete("1.0", END)
            definition_txt.insert(END, "This word does not exist. Please double check it.")
            return None

    greeting_lbl = Label(text="This is a english dictionary.\nIf you are looking for a word you can enter it below.",
                         bg="black", fg="purple", font="none 15 bold")
    greeting_lbl.grid(column=0, row=0)

    f1 = Frame(window, bg="black")
    f1.grid(column=0, row=1)

    word_ent = Entry(master=f1, bg="Yellow")
    word_ent.grid(column=0, row=1)

    search_btn = Button(master=f1, text="Enter", bg="purple", fg="blue", command=processdata)
    search_btn.grid(column=1, row=1)

    f2 = Frame(window, bg="black", relief=SUNKEN, borderwidth=5)
    f2.grid(column=0, row=2)

    directing_lbl = Label(master=f2, text="Definition-->", bg="black", fg="purple", font="none 10 bold")
    directing_lbl.grid(column=0, row=3)

    definition_txt: Text = Text(master=f2, bg="Yellow", height=15, width=70)
    definition_txt.grid(column=1, row=3)

    window.mainloop()





