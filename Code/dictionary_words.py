
import random
import sys


def random_sentence():

    word = [line.strip() for line in open("/usr/share/dict/words")]
    user_input = sys.argv[1:]
    new_sentence = []
    counter = 0
    while counter < 5:
        new_sentence.append(word[random.randint(0, len(word) - 1)])
        counter += 1
    final_word = " ".join(new_sentence)
    print(final_word)


if __name__ == '__main__':
    random_sentence()
