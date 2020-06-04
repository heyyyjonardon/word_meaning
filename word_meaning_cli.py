import requests
import re

def get_the_meaning(word):
    res = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/{}'.format(word)).text
    pattern = re.compile(r'"definition": ".+\."')
    meaning = re.findall(pattern,res)
    if len(meaning) == 0:
        print('Word not found!')
    else:
        return meaning[0]

while True:
    word = str(input("Enter word: "))
    print(get_the_meaning(word),end='\n')
    q = input(('enter q to quit\n')).strip()
    if q.lower()=='q' or q.lower()=='quit':
        quit()
    print('------------------------------------------------------------------')