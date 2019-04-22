from histogram import get_words
import random


def test_probability(histogram):
    # created list to append results
    results = []
    # number of times I want to run the test
    number_of_times = 1000

    # add sample word to list  1000 times
    for i in range(0, number_of_times):
        results.append(sampler(histogram))
    return results


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
    test_probability(words)
