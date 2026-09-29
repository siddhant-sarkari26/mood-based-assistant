from ent import *
from mood import *
from games import*
while True:
    print()
    opt = int(input("WHAT YOU WANT TO TALK ABOUT 1: MOOD 2: ENTERTAINMENT 3: GAMES 4: EXIT: "))
    
    if opt == 1:
        print(mood())

    elif opt == 2:
        ent()

    elif opt == 3:
        games()

    else: 
        print("ENJOY YOUR DAY")