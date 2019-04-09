

def get_words(file_name):
    """THIS FUNCTION WILL GET THE WORDS FROM THE
    FILE AND SAVE THEM INSIDE AN ARRAY
    """
    # print("HAS BEEN CALLED")
    words_list = []
    with open(file_name) as file:
        # print("FILE NAME")
        # get all the words in file
        for line in file:
            list_of_words = line.strip().split(" ")
            for words in list_of_words:
                words_list.append(words)
    # print("***WORDS LIST***", words_list)
    return words_list


def get_words_counts_dict(words_list):
    word_counts = {}

    for words in words_list:
        if words in word_counts:
            word_counts[words] += 1
        else:
            word_counts[words] = 1
    return word_counts


# def get_words_counts_list(word_list):

#     new_word_list = word_list.split(" ")
#     word_count = []

#     for word in new_word_list:
#         for index in word_count:
#             if index[0] == word:
#                 index[1] += 1
#         word_count.append([word, 1])
#     return word_count


def get_words_counts_list(words_list):
    words_list.sort()
    new_words_list = []

    for word in words_list:

        if len(new_words_list) is 0:
            new_words_list.append([word, 1])
        else:
            if word == new_words_list[-1][0]:
                new_words_list[-1][1] += 1
            else:
                new_words_list.append([word, 1])

    return new_words_list

    # new_words_list.remove(words)
    # new_words_list.append([words, 1])
    # for i in range(0, len(new_words_list)):
    #     if new_words_list[i][0] == words:
    #         new_words_list[i][1] += 1
    #         del new_words_list[-1]

    # for words in words_list:
    #     word_counts.append([words])
    #     if words in word_counts:
    #         print("***HAS BEEN HIT***!")
    #         word_counts[words][1] += 1

    #         print("****WORDS****", word_counts[words][1])
    # return word_counts


#         # else:
#         word_counts[words][1] += 1
#         print("WORDS LIST COUNT", word_counts[0])
#     return word_counts
    # sort words_list
    # create empty array
    # check if word is in list
    # if it is set word to none
    # then update last item value += 1
    # otherwise update array
    # then return it
if __name__ == "__main__":

    words_list = get_words('animals.txt')
    words_counts = get_words_counts_list(words_list)
    print("WORDS COUNT", words_counts)
