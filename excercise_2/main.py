if __name__ == "__main__":
    n = int(input('Enter a number: '))

    if n % 2 == 0:
        if n % 4 != 0:
            print(f'Great! Your number {n} is even')
        else:
            print(f'Looks like {n} is relative to 4')
    else:
        print(f'Oh no! Your number {n} is odd')
