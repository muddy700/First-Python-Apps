from random import randint

print("\n  GUESS THE NUMBER")
print("  Guess Between 0 - 20")

def the_Game(tries):

    while tries > 0:
        answer = randint(0, 20)
        guessed = input("\n What Is The Next Number ? : > ")
    
        if not guessed.isdigit():
            print(" Please Enter A Valid Number")
            tries -= 1
        elif int(guessed) > 20 or int(guessed) < 0:
            print(" Enter A Number Between 0 - 20")
            tries -= 1
        elif int(guessed) > answer:
            print(" Too High From Answer")
            print(" The Answer Was => ", answer)
            tries -= 1
        elif int(guessed) < answer:
            print(" Too Low From Answer")
            print(" The Answer Was => ", answer)
            tries -= 1
        elif int(guessed) == answer:
            print(" Congratulations!, You WON!\n")
            selections()
    print("\n GAME OVER!\n")
    selections()

def selections():
    option = input(' Type "play" to Play Again, or "exit" to Quit : > ')
    if option == 'play':
        the_Game(5)
    elif option == 'exit':
        print("\n See You Next Time Buddy!")
        exit()        
    else:
        selections()

the_Game(5)