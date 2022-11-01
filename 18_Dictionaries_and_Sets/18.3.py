def word_count(words):
    word_count_dictionary = {}
    for word in words:
        if word in word_count_dictionary:
            word_count_dictionary[word] = word_count_dictionary[word] + 1
        else:
            word_count_dictionary[word] = 1
    return word_count_dictionary


def main():
    words = ['Paris', 'in', 'the', 'the', 'spring']
    word_count_dictionary = word_count(words)
    print(word_count_dictionary)


main()
