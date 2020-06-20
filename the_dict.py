import json
import difflib
from difflib import get_close_matches


def returnvalue(file):
    data = json.load(open(file))
    print("""This is a english dictionary. 
If you are looking for a word you can enter it below. 
You can end the application with '\end'.\n""")
    while True:
        key_input = input("Enter Word: ")
        if key_input == "\end":
            return "Thanks for using this program!"
        elif key_input.lower() in data:
            new_key_input = key_input.lower()
        elif key_input.capitalize() in data:
            new_key_input = key_input.capitalize()
        elif key_input.upper() in data:
            new_key_input = key_input.upper()
        else:
            new_key_input = key_input
        if new_key_input in data:
            definition = data[new_key_input]
            print(' \n'.join(definition))
            continue
        elif len(get_close_matches(new_key_input, data.keys())) > 0:
            yes_or_no = input('Did you mean this word instead?: {}. Enter Y for Yes, N for No: '.format(get_close_matches(new_key_input, data.keys())[0]))
            if yes_or_no == "Y" or yes_or_no == "y":
                definition = data[get_close_matches(new_key_input, data.keys())[0]]
                print(' \n'.join(definition))
                continue
            elif yes_or_no == "N" or yes_or_no == "n":
                print("What word do you mean instead?")
            else:
                print("please try again")
                continue
        else:
            print("This word does not exist. Please double check it.")
            continue

file = "data.json"
print(returnvalue(file))



