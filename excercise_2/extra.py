if __name__ == "__main__":
    num = int(input('Enter a number: '))
    check = int(input('Enter another number: '))

    if num % check == 0:
        print(f'Great! Your number {num} can be divided by {check}')
    else:
        print(f'Oh no! Your number {num} is not a multiple of {check}')
