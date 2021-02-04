from random import choice

NUMBERS = "1234567890"
ALPHABET = ("ABCDEFGHIJQLMNOPQRSTWXYZ")
SYMBOLS = "!#$%&/()=?¡*"

def generate_password(len_pass: int):
    if len_pass < 8:
        raise Exception("You have to enter a number bigger than 8")

    numbers = lambda: choice(tuple(NUMBERS))
    letters = lambda: tuple(map( choice([str.lower,str.upper]),choice(tuple(ALPHABET))))[0]
    symbols = lambda: choice(tuple(SYMBOLS))
    choices = [letters, numbers, symbols]

    password = "".join((choice(choices)() for i in range(len_pass))) #Selector

    return password

if __name__ == "__main__":
    len_pass = int(input("Give me a length for a password (Greater than 7): "))
    password = generate_password(len_pass)

    print(password)
