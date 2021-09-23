

def sum_n(n):
    """
    Using a for loop, sum integers from 0
    through n

    :param: n is the last digit to add to the sum
    :return: the sum of digits from 0 through n
    """
    sum = 0

    for i in range(n+1):
        sum += i

    return sum



def first_two(s):
    """
    Given a string, return the first two characters
    of it without using a loop

    :param: s is a string
    :return: the first two chars of s
    """

    return s[:2]


def real_len(s):
    """
    Given a string, give the number
    of characters, without considering
    whitespace at either end

    :param: s is a string
    :return: the length without extra whitespace
    """

    return len(s.strip())


def comma_sum(s):
    """
    Given a string of comma separated
    values, return the sum of the lengths
    of each string

    :param: s is a string with CSVs
    :return: each substring's length summed
    """

    sum = 0
    for token in s.split(","):
        sum += len(token)

    return sum


def last_index(s):
    """
    Given a string, return the
    last valid index in it

    :param: s is a string
    :return: the last valid index of s
    """
    return len(s)-1