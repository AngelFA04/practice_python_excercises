def is_palindrome(string):
    def transf(x): return ''.join(x.split(' ')).lower()

    return transf(string)[::-1] == transf(string)


if __name__ == "__main__":

    string = input('Enter a string: ')

    if is_palindrome(string):
        print(f'{string} is a palindrome')
    else:
        print(f'{string} is NOT a palindrome')
