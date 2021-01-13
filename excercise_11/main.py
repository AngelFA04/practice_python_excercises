def is_prime(n):
    is_prime = True
    for i in range(2, number):
        if number%i == 0:
            is_prime = False
            break

    return is_prime

if __name__ == "__main__":
    number = int(input("Enter a number: "))

    is_prime = is_prime(number)

    print(f'The number {number} is prime? {is_prime}')
