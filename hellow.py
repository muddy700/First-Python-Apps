# place `import` statement at top of the program
from random import randint
# from random import choice
from random import seed
import math

        # Example One
# print('Hellow, Muddy')
# x = int (input('Please Enter A Number : '))
# if x < 0 :
#     x = 0
#     print('Negative Changed To Zero')
# elif x == 0 :
#     print('Zero')
# elif x == 1 :
#     print('Single')
# elif  x == 2 :
#     pass
# else :
#     print('More Than One')


        # Example Two
# size = int ( input ('Enter A Number : '))

# def counter(n) :
#     result = []
#     a , b = 0 , 1
#     while a < n  :
#         result.append(a)
#         # print(a , end=' ')
#         a , b = b , a + b
#     # return result
#     print(result)

# counter(size)


            # Example Three

# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         print(reminder)
#         if retries < 0:
#             raise ValueError('invalid user response')

# # ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
# # ask_ok('Are U Sure To Delete This File')

            # Example Four

# def guessNumber(tries):
#     while tries > 0 :
#         answer = random.randint(0, 15)
#         guessed = int (input (' \nGuess, What Is The Next Number? : '))
#         if guessed == answer :
#             print('Conglaturation!, You Won')
#             print('The Answer Was => ', answer)
#             tries = 0
#         elif guessed > answer:
#             print('Sorry!, The Number Is Too High')
#             print('The Answer Was => ', answer)
#             tries -= 1
#         elif guessed < answer:
#             print('Sorry!, The Number Is Too Low')
#             print('The Answer Was => ', answer)
#             tries -= 1
#         if tries > 0:
#             print('\n  Try Again...')
#     print('\n GAME OVER! \n ')
#     option = int (input(' 1.Play Again \n 2.Exit \n  : '))
#     if option == 1 :
#         guessNumber(3)
#     else :
#         print('\n See You Next Time Buddy! \n')

# guessNumber(3)

        # Example Five
# habitat = ['camel' , 'lion' , 'deer' , 'goose' , 'bat' , 'rabbit']
# number = int(input('Please enter the number of the habitat you would like to view: > '))
# print(habitat[number])
# print("""\n---
# You've reached the end of the program. To check another habitat, please restart the watcher.
# """)

        # Example Six
# a = b = True
# print(not a or b)
# print((a or b) and not (a and b))
# print((a and b) or not (a or b))
# print((a and not b) or (not a and b))
# print(a and not b )

        # Example 7
# print("Hello! My name is Muddy.")
# print("I was created in 2020.")
# name = input("Please, remind me your name. : ")
# print("What a great name you have, ", name + "!")

        # Example 8
# print("Hello! My name is Muddy.")
# print("I was created in 2020.")
# name = input("Please, remind me your name. \n > ")
# print("What a great name you have, ", name + "!")
# print("Let me guess your age.")
# print("Enter remainders of dividing your age by 3, 5 and 7.")
# remainder3 = int(input())
# remainder5 = int(input())
# remainder7 = int(input())
# age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
# print("Your age is ", age, "; that's a good time to start programming!")
# print("Now I will prove to you that I can count to any number you want.")
# number = int(input())
# i = 0
# while i <= number:
#     print(i, "!")
#     i += 1
# print("Let's test your programming knowledge.")
# print("Why do we use methods?")
# print("1. To repeat a statement multiple times.")
# print("2. To decompose a program into several small subroutines.")
# print("3. To determine the execution time of a program.")
# print("4. To interrupt the execution of a program.")
# # answer
# while True:
#     answer = int(input("> "))
#     if answer == 2:
#         print("Completed, have a nice day!")
#         print("Congratulations, have a nice day!")
#         break
#     else:
#         print("Please, try again.")

        # Example 9 
# print(math.log(10))
# colors = ['red', 'blue', 'green', 'black']
# print(choice(colors))

# n = int(input())

# # put your code here
# seed(n)
# print(randint(-100, 100))

        # Example 10
# import random

# # your sentence is assigned to the variable
# sentence = input().split()

# # write your python code below
# random.seed(43)
# random.shuffle(sentence)


# # shows the message
# print(' '.join(sentence))

        # Example 11
import random

print("H A N G M A N")
def game():

        words = ['python', 'java', 'kotlin', 'javascript']
        chosen = random.choice(words)
        selected = set(chosen)
        guessed = list("-" * len(chosen))
        wrong_Letters = []

        status = input('Type "play" to play the game, "exit" to quit: > ')
        if status == 'play':
                tries = 8
        else:
                game()

        while tries > 0:
                print()
                print(''.join(guessed))   
                letter = input("Input a letter: > ")

                if len(letter) != 1:
                        print("Enter Single Character")
                        tries -= 1
                elif letter in  wrong_Letters:
                        print("You've already guessed this letter")
                        tries -= 1
                elif letter not in  selected:
                        print("That letter doesn't appear in the word")
                        wrong_Letters.append(letter)
                        tries -= 1
                elif letter in selected:
                        for k in range(len(chosen)):
                                if letter == chosen[k]:
                                        guessed[k] = letter
                                        wrong_Letters.append(letter)

        print('\n \n')
        game()

game()

#     lives = 8
#     while lives > 0:
#         print("\n" + ''.join(answer))
#         guess = input("Input a letter: > ")
#         if len(guess) != 1:
#             print("You should input a single letter")
#         elif not guess.islower():
#             print("Please enter a lowercase English letter")
#         elif guess in answer:
#             print("You've already guessed this letter")
#         elif guess in letters:
#             pos = chosen.find(guess)
#             while pos != -1:
#                 answer[pos] = guess
#                 pos = chosen.find(guess, pos + 1)
#                 if ''.join(answer) == chosen:
#                     break
#         else:
#             print("That letter doesn't appear in the word")
#             lives -= 1

#     print(f"You guessed the word {chosen}!\nYou survived!") if lives > 0 else print("You lost!")
#     if status == 'play':
#             game()
#     else:
#             pass


















# Write your code here
# import random

# print("H A N G M A N")
# def game():

#         words = ['python', 'java', 'kotlin', 'javascript']
#         chosen = random.choice(words)
#         selected = set(chosen)
#         guessed = list("-" * len(chosen))
#         wrong_Letters = []
#         tries = 0
#         chance = 3
#         try:
#                 status = input('Type "play" to play the game, "exit" to quit: > ')
#                 print()
#                 if status == 'play':
#                         tries = 8
#                 elif status == 'exit':
#                         return 0
#                 elif chance == 0:
#                         return 0
#                 else:
#                         while True:
#                                 chance -= 1
#                                 game()
#                                 return False
#                         else:
#                                 return 0
#         except EOFError as e:
#                 print(end="")

#         while tries > 0:
#                 print()
#                 # displayWord = ''.join(guessed)
#                 # print(displayWord)
#                 print("-" * len(chosen))
#                 letter = input("Input a letter: > ")

#                 if len(letter) != 1:
#                         print("You should input a single letter")
#                         # tries -= 1
#                         pass
#                 elif not letter.islower():
#                         pass
#                         # print("Please enter a lowercase English letter")
#                 elif letter in wrong_Letters:
#                         # print("You've already guessed this letter")
#                         tries -= 1
#                 elif letter not in  selected:
#                         # print("That letter doesn't appear in the word")
#                         wrong_Letters.append(letter)
#                         tries -= 1
#                 elif letter in selected:
#                         for k in range(len(chosen)):
#                                 if letter == chosen[k]:
#                                         guessed[k] = letter
#                                         wrong_Letters.append(letter)
#                 elif '-' not in guessed:
#                         print("You survived!")
#                         tries = 0

#         print("\nThat letter doesn't appear in the word\nYou lost!\n")
#         # print('\n')
#         game()

# game()