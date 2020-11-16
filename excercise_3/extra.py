if __name__ == "__main__":
    arr = input().split()
    limit = int(input('Enter the max number for the list elements: '))
    arr_smaller = [n for n in arr if n < limit]
