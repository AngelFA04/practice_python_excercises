import datetime

if __name__ == "__main__":
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    number_copies = int(input('Enter a number: '))

    current_year = datetime.datetime.now().year
    year_100 = (100 - age) + current_year
    print(f'Hello, {name}, in {year_100} you will turn 100 years old.\n' *
          number_copies)
