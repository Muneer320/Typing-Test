import random
import time
from datetime import datetime as dt


print("\nWelcome to the Typing Test by Muneer.\n\n")


name = input("Enter your name: ")
mistakes = 0



with open("wordsFile.txt", "r") as f:
    sentence = random.choice(f.readlines())

print("\n\nYour sentence is: " + sentence)

ready = input("\nPress enter and start typing the above sentence (Case sensitive), press enter again when you finish...")

start = time.time()
userSentence = input("")
timeTaken = int(time.time() - start)
if timeTaken < 0:
    timeTaken = 1


for x in range(max(len(userSentence), len(sentence))):
    try:
        if userSentence[x] != sentence[x]:
            mistakes += 1
    except:
        mistakes += 1

correct = len(sentence)-mistakes
gross = len(userSentence.split())/(timeTaken/60)
net = (len(userSentence.split()) - mistakes)/(timeTaken/60)
if gross < 0 :
    gross = 0
if net < 0 :
    net = 0

accuracy = (correct / len(sentence)) * 100
currdate = dt.now()



print(f'''

====================STATS====================
Time Taken: {timeTaken} seconds
Mistakes: {mistakes}
Correct Characters: {correct}
Gross WPM: {gross}
Net WPM: {net}
Accuracy: {accuracy}
=============================================

''')

save = input("Would you like to save your Stats? (y/n): ")
if save != "y":
    pass
else:
    with open("stats.txt", "a") as f:
        f.write(f"{name.replace(' ', '_')} {currdate} {gross} {net} {accuracy}\n")

    print("Stats saved in stats.txt\n\n")



show = input("Would you like to see earlier stats? (y/n): ").lower()
if show != 'y':
    exit()
else:
    print("\n\n=================SCOREBOARD=================\n")
    with open("stats.txt", "r") as f:
        data = f.readlines()
        for x in data:
            line = x.split()
            print(f'''Name: {line[0].replace("_", " ")}
Date: {line[1]}
Time: {line[2][:8]}
Gross WPM: {line[3][:4]}
Net WPM: {line[4][:4]}
Accuracy: {line[5][:4]}
*******************************************
''')
    print("============================================")


input()