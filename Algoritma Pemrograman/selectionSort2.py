# Selection Sort Algorithm

# create array of length 'size', each element is
# randomly selected from the range (0, max)

def create_array(size=10, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]

# print(create_array()

# perfoms the selection sort algorithm on the passed
# list, return the sorted version


def selection_sort(a):
    sort_len = 0  # length of current sorted portion
    while sort_len < len(a):
        min_idx = None  # index of smallest item found
        for i, elem in enumerate(a[sort_len:]):
            # check current elem  to see if smallest
            if min_idx == None or elem < a[min_idx]:
                # update with current smallest
                min_idx = i + sort_len
        a[sort_len], a[min_idx] = a[min_idx], a[sort_len]
        sort_len += 1
    return a


# def randomNum(s=20, m=40):
#     from random import randint
#     return [randint(s, m) for _ in range(s)]


# print(randomNum())
a = create_array()
print('unsorted:', a)
a = selection_sort(a)
print('sorted:', a)
