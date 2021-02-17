def read_file(file_name):
    """
    Return a list with all the lines of a text file.
    """
    lines = []
    with open(file_name, "r") as f:
        lines = f.readlines()

    return [int(l.strip()) for l in lines]

if __name__ == "__main__":
    happy_numbers = read_file("happynumbers.txt")
    prime_numbers = read_file("primenumbers.txt")
    overlap_numbers = set(happy_numbers).intersection(set(prime_numbers))

    print(overlap_numbers)
