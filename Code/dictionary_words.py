
import random
import sys

# open the file and gets the words


def get_words(file_name):
    """ remove white space then loops over the whole file and saves it
    to words 
    """
    words = [line.strip() for line in open(file_name)]
    return words


def random_sentence(words_list, num_words):
    try:

        # create an  empty array to store words
        new_words = []
        # loop over the number of words the user gives
        for _ in range(0, num_words):
            # create random index
            random_index = random.randint(0, len(words_list) - 1)
            # append the random word the array
            new_words.append(words_list[random_index])
        # join all the words in the array to form a sentence
        final_sentence = " ".join(new_words)
        # return the sentence
        return final_sentence
    except:
        print("COULD NOT GENERATE SENTENCE TRY AGAIN!")


if __name__ == '__main__':

    user_input = sys.argv[0:]
    if len(user_input) < 2:
        print("COULD NOT GENERATE SENTENCE TRY AGAIN!")
    else:
        import timeit
        words = get_words("/usr/share/dict/words")
        for i in range(0,  int(user_input[2])):
            print(random_sentence(words, int(user_input[1])))
