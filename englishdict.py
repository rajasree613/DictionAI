from tkinter import *
import json
from difflib import get_close_matches #returns the closes matches of a word
from tkinter import messagebox
import pyttsx3
engine=pyttsx3.init() #creats instance of engine class

#speaker
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

#data.json is storing data in the form of dictionary. key is word and value is meaning
#difflib is a python module that contains severals easy to use functions and classes that allows users to compare sets of data



#search function
def search():
    data=json.load(open('dictionary.json'))
    word=enterwordEntry.get()
    word=word.lower()
    #to fetch the word and it's meaning from json file
    if word in data:
        meaning=data[word]
        textarea.delete(1.0,END)
        for item in meaning:
            textarea.insert(END,u' \u2022 '+item+'\n')

    #check closes matches of a word and return the list
    #if the length is >0 there are some similar words, if the length is 0 there are no similar words in the file
    elif len(get_close_matches(word,data.keys()))>0:
        close_match=get_close_matches(word,data.keys())[0] #data.keys means check the words from the file
        res=messagebox.askyesno('Confirm',f'Did you mean {close_match} instead?')
        if res==True:
            #to delete the wrong spelling from enter word box
            enterwordEntry.delete(0,END)
            enterwordEntry.insert(END,close_match)

            meaning=data[close_match] #meaning is a list

            textarea.delete(1.0,END)

            for item in meaning:
                textarea.insert(END, u'\u2022 ' + item + '\n')

        else:
            messagebox.showerror('Error','The word does not exist. Please check it again')
            enterwordEntry.delete(0,END)
            textarea.delete(1.0,END)

    #to delete words which don't exist in the dictionary
    else:
        messagebox.showinfo('Information','The word does not exist in the Dictionary')
        enterwordEntry.delete(0,END)
        textarea.delete(1.0,END)

#clear function to clear everything from the textboxs
def clear():
    enterwordEntry.delete(0,END)
    textarea.delete(1.0,END)

def wordaudio():
    engine.say(enterwordEntry.get())
    engine.runAndWait()

def meaningaudio():
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()



q=Tk()
q.title('DictionEng')
q.minsize(600, 520)
q.config(bg='#333333')
q.resizable(False,False)

#show icon on window
icon = PhotoImage(file='icon.png')
q.iconphoto(False,icon)


def dictfrontpage():
    q.destroy()
    import dictionfp



#Entryword
entrywordlabel = Label(q,text='Enter Word',bg='#333333',fg='ghostwhite',font=('Times New Roman',25,'bold'))
entrywordlabel.place(x=210,y=20)

#Entryfield
enterwordEntry=Entry(q,font=('Times New Roman',18),justify=CENTER,bg='ghostwhite',bd=2,relief=GROOVE)
enterwordEntry.place(x=60,y=75,width=360, height=67)
#enterwordEntry.focus_set()

#search button
searchimage=PhotoImage(file='search.png')
searchbutton=Button(q,image=searchimage,bd=0,bg='#333333',cursor='hand2',activebackground='#333333',command=search)
searchbutton.place(x=430,y=74)

#microphone button
speakerimage=PhotoImage(file='microphone.png')
speakerbutton=Button(q,image=speakerimage,bd=0,bg='#333333',cursor='hand2',activebackground='#333333',command=wordaudio)
speakerbutton.place(x=505,y=74)

#Meaningword
meaninglabel = Label(q,text='Meaning',bg='#333333',fg='crimson',font=('Times New Roman',25,'bold'))
meaninglabel.place(x=230,y=160)

#Textbox
textarea=Text(q,width=44,height=7,font=('Times New Roman',16),bd=2,relief=GROOVE,wrap='word')
textarea.place(x=60,y=220)

#microphone button
speakerimage2=PhotoImage(file='microphone.png')
speakerbutton2=Button(q,image=speakerimage2,bd=0,bg='#333333',cursor='hand2',activebackground='#333333',command=meaningaudio)
speakerbutton2.place(x=170,y=417)

#cancel button
cancelimage=PhotoImage(file='cancel.png')
cancelbutton=Button(q,image=cancelimage,bd=0,bg='#333333',cursor='hand2',activebackground='#333333',command=clear)
cancelbutton.place(x=260,y=417)

#exit button
exitimage=PhotoImage(file='back.png')
exitbutton=Button(q,image=exitimage,bd=0,bg='#333333',cursor='hand2',activebackground='#333333',command=dictfrontpage)
exitbutton.place(x=350,y=419)


def enter_function(event):
    searchbutton.invoke()
#press enter key to searcg
q.bind('<Return>',enter_function)

q.mainloop()
