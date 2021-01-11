import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    # We need to handle different string cases
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    # If word does not match completely, check with user for alternative
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("Did you mean %s instead? " %get_close_matches(word, data.keys())[0])
        decide = input("Press y for yes or n for no: ")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("Word doesn't exist in dictionary\n")
        else:
            return("You have entered wrong input please enter just y or n.\n")
    else:
        print("Word doesn't exist in dictionary\n")



word = input("Enter the word you want to search: ")
output = translate(word)
# Does the word has multiple meanings?
if type(output) == list:
    for item in output:
        print(" - " + item)
else:
    print(output)
