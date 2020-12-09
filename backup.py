import random

print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
chosen = random.choice(words)
letters = set(chosen)
answer = list("-" * len(chosen))
attempts = []


def game():
    lives = 8
    while lives > 0:
        print("\n" + ''.join(answer))
        guess = input("Input a letter:")
        
        if len(guess) != 1:
            print("You should input a single letter")
        elif not guess.islower():
            print("Please enter a lowercase English letter")
        elif guess in answer:
            print("You've already guessed this letter")
        elif guess in letters:
            attempts.append(guess)
            pos = chosen.find(guess)
            while pos != -1:
                answer[pos] = guess
                pos = chosen.find(guess, pos + 1)
                if ''.join(answer) == chosen:
                    break
        else:
            attempts.append(guess)
            print("That letter doesn't appear in the word")
            lives -= 1

    print(f"You guessed the word {chosen}!\nYou survived!") if lives > 0 else print("You lost!")
    status = input('Type "play" to play the game, "exit" to quit: > ')
    if status == 'play':
            game()
    else:
            pass
            
status = input('Type "play" to play the game, "exit" to quit: > ')
if status == 'play':
        game()
else:
        pass