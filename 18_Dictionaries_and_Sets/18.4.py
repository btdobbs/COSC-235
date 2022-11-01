def find_bad_words(words, good_words):
    bad_words = set()
    for word in words:
        if word not in good_words:
            bad_words.add(word)
    return bad_words


def main():
    words = ['apple', 'yoyo', 'peach', 'top']
    good_words = ['apple', 'cherry', 'peach', 'plum']
    bad_words = find_bad_words(words, good_words)
    print(bad_words)


main()
