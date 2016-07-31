from collections import OrderedDict


def compress_string(string):
    """
    :param string:
    :return:
    """
    if string is None:
        return None
    if string is '':
        return ''
    cnt = cnt_chars(string)
    compressed_string = ''
    for k,v in cnt.iteritems():
        if v != 1:
            compressed_string += k + str(v)
        else:
            compressed_string += k
    if len(compressed_string) == len(string):
        return string
    return compressed_string


def cnt_chars(string):
    """
    :param string:
    :return: dict which has counts of each char
    """
    # dictionary will not keep order(test cases in the challenge wanted order)
    # use ordered dict instead
    cnt = OrderedDict()
    for char in string:
        try:
            cnt[char] += 1
        except KeyError:
            cnt[char] = 1
    return cnt


def delete_string(string, delete_str):
    """

    :param string:
    :param delete_str: char to be deleted from string
    :return: returns new string with chars deleted
    """
    # key concept: strings are immutable (tuples, numbers, boolean, frozensets too)
    list_str = list(string)
    new_str = ''
    for char in list_str:
        if char != delete_str:
            new_str += char
    return new_str
