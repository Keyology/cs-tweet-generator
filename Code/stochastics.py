from histogram import get_words


def sampler(words):
    length = len(words)

    dictionary = {}

    for word in words:
        dictionary[word] = words.count(word)

    for key, value in dictionary.items():
        pairs = f'{key} = {value/length}'
        print(pairs)


if __name__ == '__main__':
    words = get_words('animals.txt')
    sampler(words)
