import random
import sys


user_input = sys.argv[1:]


def random_words(words):

    #rand_index = random.randint(0, len(user_input) - 1)
    #print("***USER_INPUT***", user_input)
    # print(user_input[rand_index])

    for i in range(len(words) - 1, 0, -1):
        random_index = random.randint(0, i+1)

        words[i], words[random_index] = words[random_index], words[i]

        sentence = " ".join(words)
    print(sentence)


if __name__ == '__main__':
    random_words(user_input)
