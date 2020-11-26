from random import sample


def generate_random_list(size, limit):
    return sample(range(limit), size)


def list_overlap(l1, l2):
    biggest = l1 if l1 >= l2 else l2
    return list(set([biggest[i] for i in range(len(biggest)) if biggest[i]
                in a and biggest[i] in b]))


if __name__ == "__main__":
    a = generate_random_list(20, 30)
    b = generate_random_list(20, 30)

    print(list_overlap(a, b))
