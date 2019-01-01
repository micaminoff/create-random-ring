import random
import os

# Init
init_list = []
with open('./names.txt') as f:
    for line in f:
        init_list.append(line.rstrip().lower())
random.shuffle(init_list) 

# Main program loop
while(1):
    user = input('Enter your name: ').lower()
    try:
        # Users are very good at giving wrong input
        asker_int = init_list.index(user)
        print('Your target is:', init_list[(asker_int + 1) % len(init_list)])
    except:
        print('Invalid input. Try again. If the problem persists, get Michael.')
        continue
    input('Press ENTER to indicate you have memorized the answer and are prepared to clear the screen.')
    os.system('clear')