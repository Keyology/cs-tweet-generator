import random
import sys


def random_words(words):
    # loop over array length
    try:
        for i in range(len(words)-1, 0, -1):
            # generate a random number
            random_index = random.randint(0, i)
            # swap the words based on index
            words[i], words[random_index] = words[random_index], words[i]
            # join the words to form a sentence
        sentence = " ".join(words)
        # print it to the user

        return sys.stdout.write(str(sentence) + '\n')
    except:
        print("COULD NOT SHUFFLE WORDS, TRY AGAIN!")


if __name__ == '__main__':

    user_input = sys.argv[1:]

    if(len(user_input) < 2):
        print("COULD NOT SHUFFLE WORDS TRY AGAIN!")
    else:
        random_words(user_input)
        user_input.clear()
