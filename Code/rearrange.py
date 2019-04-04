import random
import sys


user_input = sys.argv[1:]


def random_words(words):
    # loop over array length
    try:
        for i in range(len(words) - 1, -1,  -1):
            # generate a random number
            random_index = random.randint(0, i+1)
            # swap the words based on index
            words[i], words[random_index] = words[random_index], words[i]
            # join the words to form a sentence
        sentence = " ".join(words)
        # print it to the user

        user_input.clear()
        return sys.stdout.write(str(sentence) + '\n')
    except:
        print("COULD NOT SHUFFLE WORDS, TRY AGAIN!")


if __name__ == '__main__':

    random_words(user_input)
