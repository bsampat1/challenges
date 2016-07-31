def bubble_sort(list_):
    """
    Implement bubble sort
    The bubble sort gets its name because elements tend to move up
    into the correct order like bubbles rising to the surface.
    Bubble sort is a simple sorting algorithm.
    It works by repeatedly stepping through the list to be sorted,
    comparing each pair of adjacent items and swapping them if they are in the wrong order.
    The pass through the list is repeated until no swaps are needed,
    which indicates that the list is sorted. Because it only uses comparisons to operate on elements,
    it is a comparison sort.
    :param list_:
    :return:
    """
    for i in xrange(len(list_)):
        for j in xrange(i+1, len(list_)):
            if list_[i] > list_[j]:
                list_[i], list_[j] = list_[j], list_[i]
    return list_

def selection_sort(list_):
    """
    Implement selection sort
    Its called selection sort because we are selecting one element
    at a time(minimum)

    Find the minimum value in the list
    Swap it with the value in the first position
    Repeat the steps above for the remainder of the list (starting at the second position and advancing each time)

    :param list_:
    :return:
    """
    # Traverse through all array elements
    for i in xrange(len(list_)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in xrange(i+1, len(list_)):
            if list_[j] < list_[min_idx]:
                min_idx = j
        # Swap the found minimum element with
        # the first element
        list_[i], list_[min_idx] = list_[min_idx], list_[i]

    return list_


def quick_sort(list_):

    return list_


def merge_sort(list_):

    return list_


def insertion_sort(list_):

    return list_

def binary_search(list_, target):
    """

    :param list_:
    :param target:
    :return:
    """
    lo = 0
    hi = len(list_) - 1
    while lo <= high:
        mid = lo + ((high - lo)/2)
        if list_[mid] == target:
            return mid
        elif list_[mid] < target:
            lo = mid + 1
        else:
            high = mid - 1
    return None

# What are stacks
# What are queues
# Linked Lists implementation, deletion of node,elements, insertion etc
# Trees - BST, Djikstra's Algorithm
