

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
    # create an empty dict
    word_counts = {}

    # loop over words in list
    for words in words_list:
        # check if word is in word counts dict
        if words in word_counts:
            # if it is increase the value by 1
            word_counts[words] += 1
        else:
            # otherwise set the value to 1
            word_counts[words] = 1
    return word_counts


def get_words_counts_list(words_list):
    # sort the list
    words_list.sort()
    # create empty list
    new_words_list = []
    # loop over words list
    for word in words_list:
        # check if nothing is in the list
        if len(new_words_list) is 0:
            # if nothing is in the list append to the list
            new_words_list.append([word, 1])
        else:
            # otherwise check if word is the same as the last value added to the list
            if word == new_words_list[-1][0]:
                # increase the last value by 1
                new_words_list[-1][1] += 1
            else:
                # otherwise append to the list
                new_words_list.append([word, 1])

    return new_words_list


def get_words_counts_tuple(text):
    # create empty list
    words = []
    # get words froms list
    for word in text:
        # check if word is found
        found = False
        # looping through list
        for index in words:
            # check if word is in list
            if index[0] == word:
                #  increase list value
                freq = index[1] + 1
                # remove duplicates
                words.remove(index)
                # append word and value
                words.append((word, freq))
                # check if word is found
                found = True
        if not found:
            # if word is not found append list
            words.append((word, 1))

    return words


def unique_words(histogram):
    # returns number of unique words in histogram
    total_count = sum(histogram.values())
    return total_count


def frequency(word, histogram):
    # checks if word is in histogram
    if word in histogram:
        # returns key value pairs
        return histogram[word]
    else:
        return "That word is not in the histogram"


if __name__ == "__main__":

    words_list = get_words('animals.txt')
    words_counts = get_words_counts_list(words_list)
    new_tuple = get_words_counts_dict(words_counts)
    print("WORDS COUNT", new_tuple)
