import json

def get_dictionary_from_json():
    with open("birthdays.json", mode="r") as f:
        data = f.read()
        if data:
            PEOPLE_BIRTHDAY = json.loads(data)
        else:
            PEOPLE_BIRTHDAY = {}
    return PEOPLE_BIRTHDAY

def update_birthdays(person, birthday):
    PEOPLE_BIRTHDAY.update({person: birthday})
    with open("birthdays.json", mode="w+") as f:
        f.write(json.dumps(PEOPLE_BIRTHDAY))


def main():
    print("Welcome to the birthday dictionary. We know the birthdays of:")

    for person in PEOPLE_BIRTHDAY.keys():
        print(person)

    print("Enter [0] if you want to get the birthday of someone in the dictionary.")
    print("Enter [1] if you want to add someone new")
    choice = input()

    if choice == "0":
        person = input("Who's birthday do you want to look up?\n")
        print(get_birthday(person))
        print("Thank you!")
    elif choice == "1":
        name = input("What's the name? ")
        birthday = input("When it's her birthday? ")
        update_birthdays(name, birthday)
    else:
        print("Invalid choice!")


def get_birthday(person):
    date = PEOPLE_BIRTHDAY.get(person)
    if date:
        return f"{person}'s birthday is {date}"
    return f"{person} is not in the database!"

if __name__ == "__main__":
    PEOPLE_BIRTHDAY = get_dictionary_from_json()
    main()
