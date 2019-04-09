
# def get_words(file_name):
#     """Open a file and return all words in it.
#     """
#     words_list = []
#     with open(file_name) as file:
#         for line in file:
#             animals_list = line.strip().split(" ")
#             for animal in animals_list:
#                 words_list.append(animal)
#     return words_list


# def count_animals(animals_list):
#     """Count the occurences in a give list of animals then
#     return the data structures """

#     animals_counts = {}
#     for animal_name in animals_list:
#         if animal_name in animals_counts:
#             animals_counts[animal_name] += 1
#         else:
#             animals_counts[animal_name] = 1

#     return animals_counts


# if __name__ == "__main__":
#     animals_list = get_words("animals.txt")
#     counts = count_animals(animals_list)
#     print("COUNTS", counts)
#     for key, value in counts.items():
#         print("{} || {}".format(key, value))
#         # total = sum(value)
#         # print(" TOTAL || {}".format(total))


def get_words(file_name):
    """THIS FUNCTION WILL GET THE WORDS FROM THE
    FILE AND SAVE THEM INSIDE AN ARRAY
    """
    print("HAS BEEN CALLED")
    words_list = []
    with open(file_name) as file:
        print("FILE NAME")
        # get all the words in file
        for line in file:
            list_of_words = line.strip().split(" ")
            for words in list_of_words:
                words_list.append(words)
    return words_list


def get_words_counts_dict(words_list):
    word_counts = {}

    for words in words_list:
        if words in word_counts:
            word_counts[words] += 1
        else:
            word_counts[words] = 1
    return word_counts


# def get_words_counts_list(words_list):
#     word_counts = []

#     for words in words_list:
#         word_counts.append([words, 0])
#         # if words in word_counts:
#         #     print("***HAS BEEN HIT***!")
#         #     # word_counts[words][1] += 1
#         #     word_counts[words][1] += 1
#         #     print("****WORDS****", word_counts[words][1])

#         # else:
#         word_counts[words][1] += 1
#         print("WORDS LIST COUNT", word_counts[0])
#     return word_counts


def get_words_counts_list(words_list):
    words_counts = []

    for words in words_list:
        words_counts.append([words, 0])
        for i in range(0, len(words_counts)):
            if words_counts[i][0] == words:
                words_counts[i][1] += 1
            else:
                words_list[1] = 0
    return words_counts


if __name__ == "__main__":

    words_list = get_words('animals.txt')
    words_counts = get_words_counts_list(words_list)
    print("WORDS COUNT", words_counts)
