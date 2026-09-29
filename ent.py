def ent():
    print("SURE LETS TALK ABOUT YOUR ENTERTAINMENT")
    
    t=input("ENTER WOULD YOU LIKE TO WATCH MOVIE YES OR NO ")
    if(t=="YES"):
        k=input("FUNNY OR HORROR OR THRILLING")
        
        if(k=="FUNNY"):
            print("NICE CHOICE! WATCH 3 IDIOTS FOR NOSTALGIA AND ENTERTAINMENT , GOLMAAL , PHIR HERA PHERI")
        elif(k=="HORROR"):
            print(" GREAT CHOICE !YOU CAN WATCH 1 BHOOL BHULAIYA 2 1920")
        elif(k=="THRILLING"):
            print(" WONDERFUL YOU CAN WATCH THE BLOCKBUSTER DHURANDHAR ")
    elif(t=="NO"):
        print("TRY TO PLAY GAMES")
    else:
        print("WRONG INPUT")
