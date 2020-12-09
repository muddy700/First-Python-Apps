from random import choice

print("\n H A N G M A N")

def game(tries):
        words = ['python', 'java', 'kotlin', 'javascript', 'brunga', 'ujasi', 'supplementary', 'dulla', 'coder', 'cive', 'love', 'song']
        chosen = choice(words)
        selected = set(chosen)
        guessed = list("-" * len(chosen))
        wrong_Letters = []

        while tries > 0:
                print()
                print("", ''.join(guessed))   
                letter = input(" Input a letter: > ")

                if len(letter) != 1:
                        print(" Enter Single Character")
                        tries -= 1
                        wrong_Letters.append(letter)
                elif letter in  wrong_Letters:
                        print(" You've already guessed this letter")
                        tries -= 1
                elif not letter.islower():
                        print("Enter Lowercase Letters")
                        tries -= 1
                elif letter not in  selected:
                        print(" That letter doesn't appear in the word")
                        wrong_Letters.append(letter)
                        tries -= 1
                elif letter in selected:
                        for k in range(len(chosen)):
                                if letter == chosen[k]:
                                        guessed[k] = letter
                                        wrong_Letters.append(letter)
                if '-' not in guessed:
                        print("\n", ''.join(guessed), "\n")
                        print(" YOU WON! \n")
                        selections()

        print("\n GAME OVER! \n")
        selections()

def selections():
        option = input(' Type "play" to play the game, "exit" to quit: > ')
        if option == 'play':
                game(8)
        elif option == 'exit':
                print("\n See You Next Time Buddy!")
                exit()
        else:
                selections()
                # option = input(' Type "play" to play the game, "exit" to quit: > ') call it two times
                
selections()