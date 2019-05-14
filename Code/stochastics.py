from histogram import get_words
from histogram import get_words_counts_dict
import random


# def test_sampler(histogram, number):
#     # created list to append results
#     result = []
#     # the number of times I want to run the test

#     # appending sample word to list n times
#     for i in range(0, number):
#         result.append(sampler(histogram))
#     return result


# def test_sampler(histogram, number):

#             number_wins[key] += 1
#         else:
#             number_wins[key] = 1
#     print("NUMBER OF WINS", number_wins)


def test_sampler(words, number):
    number_wins = {}

    #  for key, value in dictionary.items():
    #     pairs = f'{key} = {value/length}'
    #     print(pairs)
    #     break

    for i in range(0, number):
        result = sampler(words)
        if result in number_wins:
            number_wins[result] += 1
        else:
            number_wins[result] = 1
    return number_wins


def sampler(words):
    length = len(words)

    dictionary = words

    # for word in words:
    #     dictionary[word] = words.count(word)

    random_value = random.random()
    total_value = sum(dictionary.values())
    total = 0
    # number_wins = {}

    for key, value in dictionary.items():
        total += value
        if total/total_value >= random_value:
            return key
            # if key in number_wins:
            #     number_wins[key] += 1
            # else:
            #     number_wins[key] = 1
            # break


if __name__ == '__main__':
    words = get_words('animals.txt')
    histogram_dict = get_words_counts_dict(words)

    # sampler(words)
    print(test_sampler(words, 10000))
