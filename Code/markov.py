import random
from dictogram import Dictogram
from histogram import get_words
from stochastics import sampler


def first_order(corpus_of_words):
    words = corpus_of_words
    chain = {}
    corpus_length = len(corpus_of_words)

    for i, key in enumerate(words):
        if corpus_length > (i + 1):
            word = words[i + 1]
            if key not in chain:
                # chain[key] = [word]
                chain[key] = Dictogram([word])
                # use dictogram class
            else:
                chain[key].add_count(word)
                # add new values using dictogram class
    return chain


def second_order(corpus_of_words):
    words = corpus_of_words  # list of strings
    chain = {}  # dict to hold Markov states, key: word, value: histogram
    corpus_length = len(words)

    for i, word1 in enumerate(words):
        if i + 2 >= corpus_length:
            break  # skip last two iterations

        word2 = words[i + 1]
        word3 = words[i + 2]
        if (word1, word2) not in chain:
            chain[(word1, word2)] = Dictogram()

        chain[(word1, word2)].add_count(word3)

    return chain


def sentencize(word_list):
    word_list[0] = word_list[0].capitalize()
    word_list.append(".")
    return " ".join(word_list)


def create_sentence(markov_chain):
    word_list = list()

    # start_word = list(markov_chain.keys())[0]
    start_word = random.choice(list(markov_chain.keys()))
    word_list.append(start_word)

    for _ in range(0, 10):
        last_word = word_list[-1]
        histogram = markov_chain.get(last_word)
        random_word = sampler(histogram)
        word_list.append(random_word)

    return sentencize(word_list)


def second_order_sentence(markov_chain):
    word_list = list()
    start_word_tuple = random.choice(list(markov_chain.keys()))
    for start_word in start_word_tuple:
        word_list.append(start_word)

    track_words = start_word_tuple

    for _ in range(0, 12):
        histogram = markov_chain.get(track_words)
        random_word = sampler(histogram)
        word_list.append(random_word)
        # updating tuple of last words that I am tracking
        track_words = (track_words[-1], random_word)

    # Capitalize first word, add period and spaces
    return sentencize(word_list)


if __name__ == "__main__":
    corpus = get_words("article.txt")
    # print(second_order(corpus))
    create_first_order_markov = first_order(corpus)
    create_second_order_markov = second_order(corpus)
    print(second_order_sentence(create_second_order_markov))
    # print("FIRST ORDER CHAIN", create_markov)
    # print(create_sentence(create_first_order_markov))
