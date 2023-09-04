list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def binary_search(target, list, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2
    if list[midpoint] == target:
        return list[midpoint]
    elif target < list[midpoint]:
        return binary_search(target, list, low, midpoint - 1)
    else:
        return binary_search(target, list, midpoint + 1, high)


binary_search(1, list)