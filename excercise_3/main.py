if __name__ == "__main__":
    arr = list(map(int, input().split()))
    limit = int(input('Enter the max number for the list elements: '))
    print([n for n in arr if n < limit])

