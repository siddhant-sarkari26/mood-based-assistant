def mood():
    print("SURE LETS TALK ABOUT YOUR MOOD")
    
    p = int(input("HOW ARE YOU FEELING? 1. HAPPY 2. SAD 3. NEED A QUOTE FOR THE DAY 4. BORED: 5:Angry "))

    if p == 1:
        return "THAT'S GREAT! keep enjoying the moment and spread your happiness"
    elif p == 2:
        return "It's okay to be sad take some restor talk to someone"
    elif p == 3:
        return "YOU HAVE TO DREAM BEFORE YOUR DREAM CAN COME TRUE - APJ ABDUL KALAM"
    elif p == 4:
        return "I can suggest indoor and outdoor games for you. Press 3(GAMES)next time."
    elif p == 5:
        return "Take a deep breath,calm down and give yourself time before reacting"
