# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 20:05:56 2021

@author: filip
"""
from tkinter import *
import os
import speech_recognition as sr
from gtts import gTTS
import pydub
from scipy.io import wavfile
from tkinter import filedialog




# Gloabal variables
gpath = ""
gfilename = ""
 # Set the languages for each person
language_change = ["en-US", "ro-RO", "en-US", "ro-RO","en-US", "ro-RO","en-US", "ro-RO","en-US", "ro-RO","en-US", "ro-RO","en-US", "ro-RO"]
# functia deschide un file de tip wav si seteaza path-ul global si numele global pentru functia start_game
def open_file():
    global gpath, gfilename
    #Select the Imagename from a folder
    t1.delete(1.0,END)
    t3.delete(1.0,END)
    filepath = filedialog.askopenfilename(title = 'pen')
    gfilename = filepath.split('/')[-1].replace('.wav', '')
    
    
    if filepath.split("/")[-1].split(".")[-1] == "wav":
        t1.insert(END, filepath.split("/")[-1])
        cale = filepath.split("/")[-1]
    else:
        t1.insert(END, "Nu este fisier .wav")
    gpath = filepath
        

def start_game(persoane, start_path):
    global gfilename, language_change
    print('loading')
    t3.delete(1.0,END)
    gfilename = 'new' + gfilename
    cale = start_path
    mymono = cale
    sprec = sr.Recognizer()
    myaudiofile = sr.AudioFile(cale)
    with myaudiofile as source:
        myaudio = sprec.record(myaudiofile)
        rez = sprec.recognize_google(myaudio, language=language_change[0], show_all=False)
    
    mytext = (rez)
    myspeech = gTTS(mytext,lang = language_change[0].split("-")[0], slow = False)
    myspeech.save(gfilename + '0' + '.mp3')
    
    nume = start_path.split('/')[-1]
    midpath = start_path.replace(nume, '')
    contor = int(persoane.get())
    
    for i in range(contor - 1):
        # Recognition
        cale = midpath
        mymono = os.path.join(cale, gfilename + str(i) + '.mp3')
        sound = pydub.AudioSegment.from_mp3(mymono)
        sound.export(cale + gfilename + str(i) + '.wav', format="wav")
        sprec = sr.Recognizer()
        myaudiofile = sr.AudioFile(cale + gfilename + str(i) + '.wav')
        with myaudiofile as source:
            myaudio = sprec.record(myaudiofile)
            rez = sprec.recognize_google(myaudio, language=language_change[i], show_all=False)
            
            # Syntesis
            mytext = (rez)
            myspeech = gTTS(mytext, lang = language_change[i].split("-")[0], slow = False)
            myspeech.save(gfilename + str(i+1)+ '.mp3')
        print('.')
    t3.insert(END, rez)
    print('finished loading')

def play_sound(persoane):
    os.system(gfilename + str(int(persoane.get()) - 1) + '.mp3')
    
    
#create empty gui
window1 = Tk()

window1.title("Telephone game")


window1.geometry("600x230+500+300")

persons = StringVar()
w1 = Label(window1, text = 'File name: ')
w1.grid(row = 0, column = 0)

t1 = Text(window1, height = 1, width = 25)
t1.grid(row = 0, column = 1)



btn1 = Button(window1, text = 'Search file', command = open_file ).grid( 
    row = 0, column = 3)



w2 = Label(window1, text = 'Number of persons:')
w2.grid(row = 1, column = 0)

e1 = Entry(window1, textvariable = persons)
e1.grid(row = 1, column = 1)



bt2 = Button(window1, text = 'Start', command =lambda: start_game(persons, gpath) ).grid( 
    row = 2, column = 0)

w3 = Label(window1, text = 'Final audio: ')
w3.grid(row = 3, column = 0)


btn3 = Button(window1, text = 'Play end audio', command =lambda: play_sound(persons) ).grid( 
    row = 3, column = 1)


w4 = Label(window1, text = "End text:")
w4.grid(row = 4, column = 0)

t3 = Text(window1, height = 1, width = 25)
t3.grid(row = 4, column = 1)



window1.mainloop()    






