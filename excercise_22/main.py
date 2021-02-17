if __name__ == '__main__':
    names = {}
    with open("nameslist.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            if names.get(line):
                names[line] += 1
            else:
                names[line] = 1

    print(names)
