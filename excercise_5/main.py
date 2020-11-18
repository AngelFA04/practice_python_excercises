from random import randint

if __name__ == "__main__":
    # Generate random lists
    l1 = [randint(0, 10) for i in range(0, randint(1, 10))]
    l2 = [randint(0, 10) for i in range(0, randint(1, 10))]

    common = set()
    greater, smaller = (lambda l1, l2: (l1, l2)
                        if len(l1) >= len(l2) else (l2, l1))(l1, l2)

    for element in greater:
        if element in smaller:
            common.add(element)

    print(list(common))
