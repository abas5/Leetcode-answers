


# Given an array of integers, return the kth frequent integer in the list


# array = [1, 2, 3, 4, 5, 5, 6]
# k = 0 --> invalid 
# k = 1 --> 5
# k = 2 --> 1 or 2 or 3 or 4 or 6


def get_most_freq(array, k):
    freq_integers = {}

    for num in array:
        if freq_integers.get(num):
            freq_integers[num] += 1
        else:
            freq_integers[num] = 1
    # freq_integers = {1:1, 2:1, 3:1, 4:1, 5:2, 6:1}

    