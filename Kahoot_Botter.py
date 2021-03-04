from kahoot import client
import random
import string
import ctypes
import os
#counter for amount of bots maybe off a little bit
def joinHandle():
  pass
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
b = 0
option = input("Enter option(1, 2, 3, 4): ")
cls()
x = int(input("Enter Kahoot ID: "))
cls()
#mormal spam
if option == "1":
    while True:
        randomn =  ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        bot = client()
        bot.join(x, randomn)
        bot.on("joined",joinHandle)
        print(randomn + " has joined!")
        b = b + 1
        ctypes.windll.kernel32.SetConsoleTitleW("Kahoot ID: {} | Amount of bots: {}".format(x, b))
#arabic letter spam
if option == "2":        
    arabic = "﷽﷽﷽﷽﷽"
    while True:
        extra = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        bot = client()
        bot.join(x, arabic + extra)
        bot.on("joined",joinHandle)
        print(arabic + extra + " has joined!")
        b = b + 1
        ctypes.windll.kernel32.SetConsoleTitleW("Kahoot ID: {} | Amount of bots: {}".format(x, b))
#self explanatory
if option == "3":
    text = 'B⠀u⠀r⠀n⠀ ⠀F⠀a⠀g⠀g⠀o⠀t⠀s! '
    while True:
        extra =  ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        bot = client()
        bot.join(x, text + extra)
        bot.on("joined",joinHandle)
        print(text + extra + " has joined!")
        b = b + 1
        ctypes.windll.kernel32.SetConsoleTitleW("Kahoot ID: {} | Amount of bots: {}".format(x, b))
#random names
if option == "4":
    text = 'fuck'
    while True:
        bot = client()
        bot.join(x, text)
        bot.on("joined",joinHandle)
        print("A bot has joined!")
        b = b + 1
        ctypes.windll.kernel32.SetConsoleTitleW("Kahoot ID: {} | Amount of bots: {}".format(x, b))