def clearConsole(): #Clear the command line
        import os
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)
def checkforimports(): #Checks if you have all modules installed if not it installs them
    def install(package):#Yes this is a custom def
        import os
        import sys
        if os.name == "nt":
            os.system(f"{sys.executable} -m pip install {package}")
        if os.name == "posix":
            os.system(f"pip install {package}")
    
    clearConsole()
    try:
        import tqdm
    except ModuleNotFoundError:
        install("tqdm")
    
    try:
        import keyboard
    except ModuleNotFoundError:
        install("keyboard")
    
    try:
        import requests
    except ModuleNotFoundError:
        install("requests")

    try:
        import random
    except ModuleNotFoundError:
        install("random")
        
    try:
        import time
    except ModuleNotFoundError:
        install("time")

    try:
        import getpass
    except ModuleNotFoundError:
        install("getpass")

    try:
        import PyDictionary
    except ModuleNotFoundError:
        install("pydictionary")

    try:
        import string
    except ModuleNotFoundError:
        install("string")
        
    try:
        import termcolor
    except ModuleNotFoundError:
        install("termcolor")

    try:
        import colorama
    except ModuleNotFoundError:
        install("colorama")
checkforimports() #calls check for imports
import sys
from tqdm import tqdm
import threading #cant really explain
import keyboard #provides keyboard support
import requests #provides list of words
import random 
import time #provides pausing options
import getpass #provides name of user
from PyDictionary import PyDictionary #provides meaning of words
import string #provides letters
from termcolor import colored #library to color text
from colorama import * #so that colored text works on windows
dictionary=PyDictionary()
init() #this is actually from colorama (i think)
from10kor100k = 10000 #option to use 10000 or 100000 word list 10000 word list is faster but less chances and  100000 is slower but more hit chances
#avg time to gen word in 10,000 = 29sec on 50 tries
#avg time to gen word in 100,000 = 2-4sec on 50 tries (but most of the time we get abbriviations of word like "olpuh") 
print(colored(rf"Hey {getpass.getuser()}, This code is attempts to generate random words and check if their real.", 'blue'))
print(colored("Press Enter To Start! Press p to pause, r to restart, by Nonja made possible by google and python discord, sponcered by wishTM (get it?\ncause wish provides shit stuf- nvm)", 'green'))
input()
print(colored('Known Errors: It returns random words which are abrivations of sentences (somtimes)', 'red'))
print(colored('prints Error: "The Following Error occured: list index out of range" but it doesnt really effect the code itself', 'red'))
print(colored('Meaning of the word parameter sometimes bugs', 'red'))
time.sleep(.5)

def randogen(N): 
    word = ''.join(random.choices(string.ascii_lowercase, k = N))
    return word
isaaadone = False
def animate():
    print(f'{Fore.LIGHTCYAN_EX}')
    progressbar = tqdm([2,4,6,8])
    for item in progressbar:
        time.sleep(.3)
        progressbar.set_description(' Loading ')
    print(f'{Fore.RESET}')
    

#all the vars
req = requests.get('https://www.mit.edu/~ecprice/wordlist.10000') #10000 faster but less hit chances and more chance of getting actual words, 100000 slower but more hit chances high chance of getting abrivations
count = 1 
another_god_damn_varible = 20000
hit = 10000
a1 =  1    
istru = 0
vor = 0
howmanywin = 0  
cont = req.text.splitlines()
cont = set(cont)
Starttime = time.time()
while istru < 3:
    if keyboard.is_pressed("r"):
        another_god_damn_varible = 20000
        vor = 0
        count = 1
        hit = 10000
        a1 = 1
        Starttime = time.time()
        istru = 0
    
    if keyboard.is_pressed("p"):
        print(colored("Press enter to continue, stop to quit", 'magenta'))
        morein = input()
        if morein.lower() == 'stop':
            quit()
    
    how_long_should_word_be = random.randint(5,10) #You can change this, this is how long any random gen'd word would be so (5,10) is a word between 5 to 10 letters
    word = randogen(how_long_should_word_be)
    word = word.lower()
    #word = '' #this is cheats lol, i used this for dev stuff
    if word in cont:
        stop_time = time.time()
        clearConsole()
        t = threading.Thread(target=animate)
        t.start()
        word_meaning = dictionary.meaning(rf"{word}")
        if word_meaning == None:
            word_meaning = colored('Meaning of the word not found', 'red')
        else:
            key_ = list(word_meaning.keys())[0]
            word_meaning = (f"{key_}: {', '.join(word_meaning[key_])}")
            word_meaning = (colored(word_meaning, 'green'))
        tx = colored(rf'Meaning of "{word}":', 'cyan')
        Time_taken = stop_time - Starttime
        Time_taken = round(Time_taken, 1)
        Time_taken -= vor
        isaaadone = True
        clearConsole()
        #meaning of words stuff done now all thats remaining is printing it
        print(colored(rf'Winning generated word: "{word}"', 'green'))
        print(colored(rf'Attempt that won: {count}', 'green'))
        print(colored(rf'Time That Took: {Time_taken} sec', 'green'))
        print(rf'{tx} {word_meaning}')
        

        print(colored('To restart press "r", to stop press anything else', 'magenta'))
        
        #if you want it to run forever u can just delete everything after this line untill "break" and add istru = 0
        
        if keyboard.read_key() == "r":
            another_god_damn_varible = 20000
            vor = 0
            count = 1
            hit = 10000
            a1 = 1
            howmanywin += 1
            Starttime = time.time()
            istru = 0
        else:
            break            
    else:
        text = colored(rf'Attempt Number: {count}', 'magenta')
        text2 = colored(rf'Word That Was Generated: "{word}"', 'red')
        print(rf'{text} {text2}')
        


    if count == hit:
        clearConsole()#calls the clear colsole function
        print(colored(rf"Hit {a1}0,000 attempts", 'green'))
        

        a1 += 1
        hit += 10000
        vor += .8
        if count == another_god_damn_varible: #idk why i even added this but i feel like this helps
            print(colored(f"Performed Auto Reset: {another_god_damn_varible}", 'cyan'))
            another_god_damn_varible += 20000
            istru = 0
        time.sleep(.8)
    
    count += 1





    


