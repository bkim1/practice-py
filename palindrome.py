def palin(word):
    for ch1, ch2 in zip(word, reversed(word)):
        if ch1 != ch2:
            return False
    return True


if __name__ == "__main__":
    word = input("Enter word: ")

    print(palin(word))
    word = input("Enter word ('q' to quit): ")
    while word != "q":
        print(palin(word))
        word = input("Enter word ('q' to quit): ")