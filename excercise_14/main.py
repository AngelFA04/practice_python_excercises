def remove_duplicates(arr: list):
    """
    Remove all duplicated elements.
    """
    count = {}
    dups = []
    # Count elements
    for i in arr:
        try:
            count[i] += 1
        except KeyError:
            count[i] = 1
    #print(count)
    for key,val in count.items():
        if val > 1:
            dups.extend([key]*(val-1))

    #print(dups)
    for i in dups:
        arr.remove(i)

    #print(arr)
    return arr



if __name__ == "__main__":
    arr = input('Enter a new list: ').split()

    print(remove_duplicates(arr))

