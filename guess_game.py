import random
random_number=random.randint(0,10)
print("Guess the random number between 1 and 10 to win! You have 5 guesses")
guess_count=1
possible_guesses = range(0, 121)
while guess_count<=5:
    try :
        guess=int(input('>>'))
    except ValueError:
        print('Invalid Error')
    if guess==random_number:
        print('you won')
        break
    elif guess<random_number:
        print('too low')
        guess_count+=1
    elif guess >random_number:
        print('too high')
        guess_count+=1
    elif guess not in possible_guesses:
        print('print a number between 1 ot 10')
else:
    print(f'you lost the game is {random_number}')
#Bla44er
