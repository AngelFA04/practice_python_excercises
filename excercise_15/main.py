def create_response(words: list):
    return " ".join(words[::-1])

if __name__ == "__main__":
    words = input("Give me a sentence: ").split()

    print(create_response(words))
