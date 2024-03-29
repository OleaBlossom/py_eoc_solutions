#!/usr/bin/env checkio --domain=epy run even-last
def even_last(array):
    """
        sums even-indexes elements and multiply at the last
    """
    try:
        return sum(x for x in array[0::2]) * array[-1]
    except IndexError:
        return 0


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(even_last([0, 1, 2, 3, 4, 5]))

    assert even_last([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert even_last([1, 3, 5]) == 30, "(1+5)*5=30"
    assert even_last([6]) == 36, "(6)*6=36"
    assert even_last([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
