from collections import defaultdict, Counter

def counts(string):
    """
    :param string:
    :return: highest count of char in a string
    http://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops-in-python
    In the case of dictionaries, it's implemented at the C level. The details are available in PEP 234. In particular, the section titled "Dictionary Iterators":

    Dictionaries implement a tp_iter slot that returns an efficient iterator that iterates over the keys of the dictionary. [...] This means that we can write

    for k in dict: ...
    which is equivalent to, but much faster than

    for k in dict.keys(): ...
    as long as the restriction on modifications to the dictionary (either by the loop or by another thread) are not violated.
    Add methods to dictionaries that return different kinds of iterators explicitly:

    for key in dict.iterkeys(): ...

    for value in dict.itervalues(): ...

    for key, value in dict.iteritems(): ...
    This means that for x in dict is shorthand for for x in dict.iterkeys().


    as others have pointed out, iterating over a dict iterates through it's keys in no particular order.

    As you can see here

    d = {'x': 1, 'y': 2, 'z': 3}
    list(d)
    ['y', 'x', 'z']
    d.keys()
    ['y', 'x', 'z']
    For your example it is a better idea to use dict.items()

    d.items()
    [('y', 2), ('x', 1), ('z', 3)]
    This gives you a list of tuples. When you loop over them like this, each tuple is unpacked into k and v automatically

    for k,v in d.items():
        print k, 'corresponds to', v
    Using k and v as variable names when looping over a dict is quite common if the body of the loop is only a few lines. For more complicated loops it may be a good idea to use more descriptive names

    for letter, number in d.items():
        print letter, 'corresponds to', number
    It's a good idea going forward to get into the habit of using format strings

    for letter, number in d.items():
        print '{0} corresponds to {1}'.format(letter, number)
    """
    freq = {}
    for char in string:
        try:
            freq[char] += 1
        except KeyError:
            freq[char] = 1
    return max_list(freq)

def max_list(freq):
    """

    :param freq: dictionary with occurences of each character
    :return: returns list of max items
    """
    # returns key of max freq
    max_list = []
    for k, v in freq.iteritems():
        if v == max(freq.values()):
            max_list.append(k)
    return max_list


def counts_defaultdict(str1):
    """
    Implemnt using defaultdict(dict subclass), which adds default value for a dict if not present
    __missing__, note that you do not need to catch exception of keyerror the first time
    a char is encountered, the default values for an int if not present is 0
    :param str1:
    :return:
    """
    a = defaultdict(int)
    for char in str1:
        a[char] += 1
    return max_list(a)


def counts_counter(str1):
    """
    Implement using Counter, dict subclass
    :param str1:
    :return:
    """
    cnt = Counter()
    for char in str1:
        cnt[char] += 1
    return max_list(dict(cnt))