import random
from dictogram import Dictogram
from histogram import get_words
from stochastics import sampler
from listogram import Listogram


def first_order(corpus_of_words):
    # print("****Corpus of words*****", corpus_of_words)
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
    words = corpus_of_words
    chain = {}
    corpus_length = len(words)

    for i, key1 in enumerate(words):
        if corpus_length > (i + 2):
            key2 = words[i + 1]
            word = words[i + 2]
            if(key1, key2) not in chain:
                chain[(key1, key2)] = Dictogram([word])

            else:
                chain[(key1, key2)].add_count(word)

    return chain


def create_sentence(markov_chain):
    sentence = list()

    # start_word = list(markov_chain.keys())[0]
    start_word = random.choice(list(markov_chain.keys()))

    sentence.append(start_word)

    for i in range(0, 10):

        get_value = markov_chain.get(sentence[-1])
        random_word = sampler(get_value)
        sentence.append(random_word)
    sentence[-1] = "."
    return " ".join(sentence)


def second_order_sentence(markov_chain):
    start_words = random.choice(list(markov_chain.keys()))
    sentence = list(start_words)
    track_words = start_words

    for _ in range(0, 12):
        get_value = markov_chain.get(track_words)
        random_word = sampler(get_value)
        sentence.append(random_word)
        track_words = (track_words[-1], random_word)
    sentence[0] = sentence[0].capitalize()
    sentence[-1] = "."
    return " ".join(sentence)


if __name__ == "__main__":
    corpus = get_words("article.txt")
    # print(second_order(corpus))
    create_first_order_markov = first_order(corpus)
    create_second_order_markov = second_order(corpus)
    print(second_order_sentence(create_second_order_markov))
    # print("FIRST ORDER CHAIN", create_markov)
    # print(create_sentence(create_first_order_markov))
