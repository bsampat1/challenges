def permutations(str1, str2):
    """
    :param str1:
    :param str2:
    :return: True if one string can be a permutation of other else False
    """
    set_str1 = set(str1)
    set_str2 = set(str2)
    if len(set_str1) != 0 and len(set_str2) != 0:
        return (set_str1.intersection(set_str2) == set_str1) or (set_str1.intersection(set_str2) == set_str2)
    elif len(set_str1) == 0 and len(set_str2) == 0:
        return True
    else:
        return False

