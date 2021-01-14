def fibonacci_numbers(n):
    """
    x_1 = 1
    x_2 = 1
    x_n = x_n-1 + x_n-2, x > 2

    1, 1, 2, 3, 5, 8, 13...
    """
    fib_numbers = []
    for i in range(0, n):
        if i == 0 or i == 1:
            fib_numbers.append(1)
        else:
            num = fib_numbers[i-1] + fib_numbers[i-2]
            fib_numbers.append(num)

    return fib_numbers

if __name__ == "__main__":
    n = int(input('How many fibonacci numbers do you want? '))

    print(fibonacci_numbers(n))
