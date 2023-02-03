#A random dice roller
#will roll a d4, d6, d8, d10, d12, d20, or d100
#by Ashley Cook

#create gui to choose a die to roll
from tkinter import *
import time
import random
root = Tk()
root.geometry('400x400')
root.title('Random Dice Roll Simulator')
Label(root, text='Random Polyhedral \nDice Simulator', font = 'terminal 20 bold', background='black', fg= 'white').pack()
Label(root, text='Choose a Die', font = 'terminal 15 bold', background='black', fg= 'white').pack()
root.configure(background ='black')
def d4():
    print("Now rolling")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    print(random.randint(1,4))
def d6():
    print("Now rolling")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    print(random.randint(1,6))
def d8():
    print("Now rolling")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    print(random.randint(1,8))
def d10():
    print("Now rolling")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    print(random.randint(1,10))
def d12():
    print("Now rolling")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    print(random.randint(1,12))
def d20():
    print("Now rolling")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    print(random.randint(1,20))
def d100():
    print("Now rolling")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    numlist = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    num10 = random.randint(1,10)
    num100part = random.choice(numlist)
    num100 = num100part + num10
    print(num100)

#create buttons for different die
Button(root, text = 'd4', font= 'terminal 20', command = d4, bg='#84c50a').place(x=60, y=120)
Button(root, text = 'd6', font= 'terminal 20', command = d6, bg='#c50a84').place(x=300, y=100)
Button(root, text = 'd8', font= 'terminal 20', command = d8, bg='#24c50a').place(x=140, y=190)
Button(root, text = 'd10', font= 'terminal 20', command = d10, bg='#8100ed').place(x=260, y=200)
Button(root, text = 'd12', font= 'terminal 20', command = d12, bg='#d13678').place(x=50, y=280)
Button(root, text = 'd20', font= 'terminal 20', command = d20, bg='#36c3d1').place(x=320, y=280)
Button(root, text = 'd100', font= 'terminal 20', command = d100, bg='#e7550c').place(x=200, y=340)

root.mainloop()
