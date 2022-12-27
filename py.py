import random
import datetime
import time
start_time = time.time()
#madmah proyekt.

#                      _          _              _       _
#  _ __ ___   __ _  __| | ___    | |__   ___    | | ___ | |_ ___ _ __ ___
# | '_ ` _ \ / _` |/ _` |/ _ \   | '_ \ / _ \   | |/ _ \| __/ _ \ '_ ` _ \
# | | | | | | (_| | (_| |  __/   | |_) |  __/   | | (_) | ||  __/ | | | | |
# |_| |_| |_|\__,_|\__,_|\___|___|_.__/ \___|___|_|\___/ \__\___|_| |_| |_|
#                           |_____|        |_____|

welcome_text = """
 ______________________
< game.started >
 ----------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||
"""
#geting the random word
def get_word():
    with open("t.txt", "r") as words:
        wrde = words.readlines()
        wrd = []
        for i in wrde:
            wrd.append(i.replace("\n", ""))   
        return random.choice(wrd).lower()
#asking the player to enter a char
def print_into(trys):
    return input(f"{trys} trys\n|\n|\n|\n|\n|\npls enter a char     :")

#checking if the chat inside the word
def check_word(char):
    global randomword
    return char in randomword

#updating the board
def replace(char):
    global msword
    global randomword
    j = 0
    for i in randomword:
        if i == char:
            msword[j] = char
        j+=1
#convert sec to time
def get_sec2time(t):
    return str(datetime.timedelta(seconds=t))
    
#check best time
def checkbesttime(t):
    arr = []
    with open("score.txt", "a") as f:
        with open("score.txt", "r") as fr:
            lines = fr.readlines()
            for i in lines:
                arr.append(i.replace("\n",""))
            if int(arr[0]) < t:
                return False
            else:
                with open("score.txt", "w") as bdfg:
                    pass
                f.write(str(t))
                return True
#save best name
def savebestname(name, t):
    if checkbesttime(t):
        with open('names.txt', 'a') as mainf:
            with open("names.txt", "w") as f:
                pass   
            mainf.write(str(name))
username = input("what is your name     :")
randomword = get_word()
msword = []
trys = 0
for i in range(len(randomword)):
    msword.append("_")
print(welcome_text)
while "_" in msword:
    #print the board
    print(msword)
    #geting the player char
    userchar = print_into(trys).lower()
    #updating the board if the player char in the word
    if check_word(userchar) and userchar != "" and len(userchar) <2:
        replace(userchar)

    #updating th trys couters
    trys +=1
t = int(time.time() - start_time)
savebestname(username, t)
print(f'you won,\nword thet you gess was:  "{randomword}".\ntime:   {get_sec2time(t)}')
