from tkinter import *
import requests
import re


meaning = []


def get_the_meaning_on_return(event):
    word = word_entry.get()
    res = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/{}'.format(word)).text
    pattern = re.compile(r'"definition": ".+\."')
    meaning = re.findall(pattern,res)

    if len(meaning) == 0:
        meaning.append('Word not found!')

    meaning_window = Tk()
    text_mean = Label(meaning_window,text=meaning[0])  
    text_mean.grid()
    ok_button = Button(meaning_window,text='OK!',command=meaning_window.destroy) 
    ok_button.grid(row=1) 
    meaning_window.mainloop()

def get_the_meaning():
    word = word_entry.get()
    res = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/{}'.format(word)).text
    pattern = re.compile(r'"definition": ".+\."')
    meaning = re.findall(pattern,res)

    if len(meaning) == 0:
        meaning.append('Word not found!')

    meaning_window = Tk()
    text_mean = Label(meaning_window,text=meaning[0])  
    text_mean.grid()
    ok_button = Button(meaning_window,text='OK!',command=meaning_window.destroy) 
    ok_button.grid(row=1) 
    meaning_window.mainloop()

tk_obj = Tk()
tk_obj.title('Man\'s search for meaning')
tk_obj.geometry('190x110')

var = StringVar()
text = Label(tk_obj,textvariable=var)
var.set('-------Hello! Enter the word-------')
text.grid(row=0)

word_entry = Entry(tk_obj)
word_entry.grid(row=1,column=0)

tk_obj.bind('<Return>',get_the_meaning_on_return)
search_button = Button(tk_obj,text="Search Meaning",command=get_the_meaning)
search_button.grid(row=2,column=0)

quit_button = Button(tk_obj,text='QUIT!',command=tk_obj.destroy)
quit_button.grid(row=3,column=0)

tk_obj.mainloop()
