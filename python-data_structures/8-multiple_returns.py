"""Return a tuple with the length of a string and its first character"""


def multiple_returns(sentence):
    try:
        return len(sentence), sentence[0]
    except IndexError:
        return 0, None
