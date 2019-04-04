
import random
import sys


def get_words(file_name):
    words = [line.strip() for line in open(file_name)]
    return words


def random_sentence(words_list, num_words):

    new_words = []
    for idx in range(0, num_words):
        random_index = random.randint(0, len(words_list) - 1)
        new_words.append(words_list[random_index])
    final_sentence = " ".join(new_words)
    return final_sentence


if __name__ == '__main__':
    user_input = sys.argv[1]
    words = get_words("/usr/share/dict/words")
    for i in range(0,  int(sys.argv[2])):
        print(random_sentence(words, int(user_input)))
