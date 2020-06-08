import requests
import re

def get_the_meaning(word):
    res = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/{}'.format(word)).text
    pattern = re.compile(r'"definition": ".+\."')
    meaning = re.findall(pattern,res)
    meaning = re.sub("definition","Meaning",meaning[0])
    if len(meaning) == 0:
        return('Word not found!')
    else:
        return meaning

while True:
    word = str(input("Enter word: "))
    print(get_the_meaning(word),end='\n')
    q = input(('enter q to quit or any key to continue\n')).strip()
    if q.lower()=='q' or q.lower()=='quit':
        quit()
    print('------------------------------------------------------------------')
