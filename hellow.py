import random
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

def guessNumber(tries):
    while tries > 0 :
        answer = random.randint(0, 15)
        guessed = int (input (' \nGuess, What Is The Next Number? : '))
        if guessed == answer :
            print('Conglaturation!, You Won')
            print('The Answer Was => ', answer)
            tries = 0
        elif guessed > answer:
            print('Sorry!, The Number Is Too High')
            print('The Answer Was => ', answer)
            tries -= 1
        elif guessed < answer:
            print('Sorry!, The Number Is Too Low')
            print('The Answer Was => ', answer)
            tries -= 1
        if tries > 0:
            print('\n  Try Again...')
    print('\n GAME OVER! \n ')
    option = int (input(' 1.Play Again \n 2.Exit \n  : '))
    if option == 1 :
        guessNumber(3)
    else :
        print('\n See You Next Time Buddy! \n')

guessNumber(3)