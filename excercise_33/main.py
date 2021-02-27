PEOPLE_BIRTHDAY = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",
    "Ada Lovelace": "12/10/1815",
}

def main():
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for person in PEOPLE_BIRTHDAY.keys():
        print(person)

    choice = input("Who's birthday do you want to look up?\n")
    print(get_birthday(choice))
    print("Thank you!")

def get_birthday(person):
    date = PEOPLE_BIRTHDAY.get(person)

    if date:
        return f"{person}'s birthday is {date}"
    return f"{person} is not in the database!"

if __name__ == "__main__":
    main()
