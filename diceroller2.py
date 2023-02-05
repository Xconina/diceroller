#A random dice roller, 2
#will roll a d4, d6, d8, d10, d12, d20, or d100
#This second version will output the results on the GUI instead of just the terminal
#by Ashley Cook

#create gui to choose a die to roll
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import time
import random
root = Tk()
root.geometry('400x400')
root.title('Random Dice Roll Simulator')
Label(root, text='Random Polyhedral \nDice Simulator', font = 'terminal 20 bold', background='black', fg= 'white').pack()
Label(root, text='Choose a Die', font = 'terminal 15 bold', background='black', fg= 'white').pack()
root.configure(background ='black')

#define different dice and what the rolls will do
def d4():
    d4output = random.randint(1,4) 
    time.sleep(0.5)  
    print(d4output) 
    labeld4 = Label(root, text= d4output, font= 'terminal 15', background='black', fg= '#84c50a').place(x=40,y=120)
def d6():
    d6output = random.randint(1,6)
    time.sleep(0.5)
    print(d6output)
    labeld6 = Label(root, text= d6output, font= 'terminal 15', background='black', fg= '#c50a84').place(x=280,y=100)
def d8():
    d8output = random.randint(1,8)
    time.sleep(0.5)
    print(d8output)
    labeld8 = Label(root, text= d8output, font= 'terminal 15', background='black', fg= '#24c50a').place(x=110,y=190)
def d10():
    d10output = random.randint(1,10)
    time.sleep(0.5)
    print(d10output)
    labeld10 = Label(root, text= d10output, font = 'terminal 15', background = 'black', fg='#8100ed').place(x=230, y=200)
def d12():
    d12output= random.randint(1,12)
    time.sleep(0.5)
    print(d12output)
    labeld12 = Label(root, text= d12output, font = 'terminal 15', background = 'black', fg='#d13678').place(x=20, y=280)
def d20():
    d20output = random.randint(1,20)
    time.sleep(0.5)
    print(d20output)
    labeld20 = Label(root, text= d20output, font = 'terminal 15', background = 'black', fg='#36c3d1').place(x=290, y=280)   
def d100():
    d100output = random.randint(1,100)
    time.sleep(0.5)
    print(d100output)
    labeld100 = Label(root, text= d100output, font = 'terminal 15', background = 'black', fg='#e7550c').place(x=180, y=340)
    
    

#create buttons for different die
Button(root, text = 'd4', font= 'terminal 20', command = d4, bg='#84c50a').place(x=60, y=120)
Button(root, text = 'd6', font= 'terminal 20', command = d6, bg='#c50a84').place(x=300, y=100)
Button(root, text = 'd8', font= 'terminal 20', command = d8, bg='#24c50a').place(x=130, y=190)
Button(root, text = 'd10', font= 'terminal 20', command = d10, bg='#8100ed').place(x=260, y=200)
Button(root, text = 'd12', font= 'terminal 20', command = d12, bg='#d13678').place(x=50, y=280)
Button(root, text = 'd20', font= 'terminal 20', command = d20, bg='#36c3d1').place(x=320, y=280)
Button(root, text = 'd100', font= 'terminal 20', command = d100, bg='#e7550c').place(x=210, y=340)


root.mainloop()
