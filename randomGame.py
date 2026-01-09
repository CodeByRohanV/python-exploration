import random
def runGame():
    attempts = 0

    while(True):
        GenNumber = random.randint(1,10)
        GuessNumber = int(input("Guess the number"))
         
        attempts+=1
        if GenNumber==GuessNumber:
            print("Correct")
            break
        elif GenNumber > GuessNumber:
            print("Too Low")    
        else:
            print("Too High")
    print("YOu had gueesed with attempts" + str(attempts))
runGame()
playagain = input("Do you want to play again? (yes/no):")
# if(playagain=="yes"):
#     runGame()
# else:
#     print("goodbye, See you tomorrow")
while playagain == "yes":
    newRandom = random.randint(1,100)
    runGame(newRandom)
    
print("goodbye, See you tomorrow")




