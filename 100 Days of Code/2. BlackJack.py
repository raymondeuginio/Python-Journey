import random
logo = " ~THIS IS BLACKJACK LOGO~ "
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def sumallcards(namalist):
    """ Fungsi menjumlahkan semua nilai kartu pada list. """
    return sum(namalist)

def finalscore():
    print(f"Your final cards:{playcards}, final score ={sumallcards(playcards)} ")
    print(f"Computer final cards:{compcards}, final score ={sumallcards(compcards)} ")   

    
def marimain():
    compcards.append(random.choice(cards))
    playcards.append(random.choice(cards))
    playcards.append(random.choice(cards))
    print(f"Your cards:{playcards}, current score = {sumallcards(playcards)} ")
    print(f"Computer's first card: {compcards}")

    pickanother = input("Pick another card? 'y' or 'n' ").lower()

    if pickanother == "y":
        playcards.append(random.choice(cards))
        print(f"Your cards:{playcards}, current score ={sumallcards(playcards)} ")
        
    elif pickanother == "n":
        while sumallcards(compcards) < 17:
            compcards.append(random.choice(cards))
        finalscore() 
        if sumallcards(playcards) == sumallcards(compcards):
            print("You Tie~")
    else:
        print("Your input is wrong")
        return
    
    if sumallcards(playcards) > 21:
        print("You lose :( ")
        finalscore()  
        return
    elif sumallcards(compcards) > 21:
        print("Computer Lost---")
        print("You Win")
        finalscore() 
        return
    
wannaplay = "y"
while wannaplay != "n":
    wannaplay = input("Do you wanna play blackjack? 'y' or 'n' ").lower()
    if wannaplay == "y":
        compcards = []
        playcards = []
        marimain()

    elif wannaplay =="n":
        break
    else:
        print("INVALID INPUT")
        break


print("\nThanks For Playing")   



    