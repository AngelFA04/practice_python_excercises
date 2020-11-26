import random

if __name__ == "__main__":

    random_number = random.randint(1, 9)
    right = False

    guess = int(input('Guess a number between 1 and 9: '))
    counter = 1

    while not right:

        if guess < random_number:
            print('Too low... Try again: ', end=' ')
        elif guess > random_number:
            print('Too high... Try again: ', end=' ')
        else:
            print('Exactly right. Excellent:D')
            break
        counter += 1

        guess = input()
        if guess == 'exit':
            break
        guess = int(guess)

    print('Total guesses: ', counter)
