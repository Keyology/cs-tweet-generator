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
                #chain[key] = [word]
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
    sentence = []

    start_word = list(markov_chain.keys())[0]

    sentence.append(start_word)

    for i in range(0, 10):
        # get
        print("SENTENCE", sentence)
        get_value = markov_chain.get(sentence[-1])
        print("***GET VALUE***", get_value)
        print("GET VALUE", get_value)
        # random_word = random.choice(get_value)
        # rename variable
        # use counts in dictogram to sample  words based on probability
        random_word = sampler(get_value)
        print("RANDOM WORDS!", random_word)
        sentence.append(random_word)
    return " ".join(sentence)


if __name__ == "__main__":
    corpus = get_words("article.txt")
    # print(second_order(corpus))
    create_markov = first_order(corpus)
    #print("FIRST ORDER CHAIN", create_markov)
    print(create_sentence(create_markov))
