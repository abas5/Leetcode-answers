

def max_subset_sum_no_adjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    
    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])

    print(maxSums)
    for i in range(2, len(array)):
        print(i)
        maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])
    
    print(maxSums[-1])
    return maxSums[-1]




max_subset_sum_no_adjacent([75, 105, 120, 75, 90, 135])