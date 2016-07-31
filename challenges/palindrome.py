def palindrome(string):
    reverse = ''
    for i in xrange(len(string)-1, -1, -1):
        reverse += string[i]
    return reverse.upper() == string.upper()


def reverse_a_list(string):
    """
    Python slicing notation:

    http://stackoverflow.com/questions/509211/explain-pythons-slice-notation
     +---+---+---+---+---+---+
     | P | y | t | h | o | n |
     +---+---+---+---+---+---+
       0   1   2   3   4   5
      -6  -5  -4  -3  -2  -1
    a[start:end:step]
    For start and end, negative values are interpreted as being relative to the end of the sequence.
    Positive indices for end indicate the position after the last element to be included.
    Blank values are defaulted as follows: [+0:-0:1].
    Using a negative step reverses the interpretation of start and end
    :param string:
    :return:
    """
    if string is None:
        return None
    return string[::-1]


