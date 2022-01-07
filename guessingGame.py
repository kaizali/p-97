import random

number = random.randint(1, 9)
chances = 0
print ('guess a number between 1 and 9')

while chances <5:
    guess = int(input('enter your guessing number'))
    if guess ==number:
        print('congratulations to you won')
        break
    elif guess<number:
        print('your guess was low.Guess a number greater than ',guess)

    else:
        print('your guess was too high.Guess a number lower than', guess)

    chances+=1

if not chances<5:
    print('you lose! The number is  ', number)