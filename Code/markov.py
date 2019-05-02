import random
from histogram import get_words


corpus = get_words("article.txt")


def word_transition(corpus_of_words):
    words = []
    words = words + corpus_of_words
    chain = {}
    corpus_length = len(corpus_of_words)

    for i, key in enumerate(words):
        if corpus_length > (i + 1):
            word = words[i + 1]
            if key not in chain:
                chain[key] = [word]
            else:
                chain[key].append(word)
    return chain


def create_sentence(markov_chain):
    sentence = []

    start_word = list(markov_chain.keys())[0]

    sentence.append(start_word)

    for i in range(0, 10):
        get_value = markov_chain.get(sentence[-1])
        random_word = random.choice(get_value)
        sentence.append(random_word)
    return " ".join(sentence)


if __name__ == "__main__":
    create_markov = word_transition(corpus)

    print(create_sentence(create_markov))
