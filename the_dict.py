import json
from difflib import get_close_matches
from KeyInput import *


def returnvalue(file):
    data = json.load(open(file))
    print("""This is a english dictionary. 
If you are looking for a word you can enter it below. 
You can end the application with '\end'.\n""")
    while True:
        KeyInput.word = input("Enter Word: ")


        if KeyInput.word == "\end":
            return "Thanks for using this program!"
        elif KeyInput.word.lower() in data:
            KeyInput.word = KeyInput.word.lower()
            KeyInput.status = True
        elif KeyInput.word.capitalize() in data:
            KeyInput.word = KeyInput.word.capitalize()
            KeyInput.status = True
        elif KeyInput.word.upper() in data:
            KeyInput.word = KeyInput.word.upper()
            KeyInput.status = True
        else:
            KeyInput.status = False


        if KeyInput.status == True:
            definition = data[KeyInput.word]
            print(' \n'.join(definition))
            continue
        elif len(get_close_matches(KeyInput.word, data.keys())) > 0:
            close_match = get_close_matches(KeyInput.word, data.keys())[0]
            yes_or_no = input('Did you mean this word instead?: {}. Enter Y for Yes, N for No: '.format(close_match))
            if yes_or_no == "Y" or yes_or_no == "y":
                definition = data[close_match]
                print(' \n'.join(definition))
                continue
            elif yes_or_no == "N" or yes_or_no == "n":
                print("What word do you mean instead?")
                continue
            else:
                print("please try again")
                continue
        else:
            print("This word does not exist. Please double check it.")
            continue


file = "data.json"
print(returnvalue(file))



