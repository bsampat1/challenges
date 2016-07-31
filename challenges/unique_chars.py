def repeat_chars(string):
    """ Returns True if string repeats else False """
    for i in xrange(len(string)):
        for j in xrange(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True


def unique_chars_set(string):
    return len(set(string)) == len(string)

