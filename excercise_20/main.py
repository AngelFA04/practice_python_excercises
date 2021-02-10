import random
def generate_sorted_list(n):
    return sorted([random.randint(0, n) for i in range(n)])

def linear_search(arr, number):
    for i in arr:
        if number == i:
            return True
    return False

if __name__ == "__main__":
    arr = generate_sorted_list(20)
    number = int(input("Give me a number to find: "))

    if linear_search(arr, number):
        print("The number is in the list!")
    else:
        print("The number is NOT in the list:(")
