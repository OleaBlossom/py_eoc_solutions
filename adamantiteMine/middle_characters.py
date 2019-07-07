#!/usr/bin/env checkio --domain=epy run middle-characters


def middle(text):
    x = len(text)
    if x % 2 == 0:
        return text[x // 2 - 1] + text[x // 2]
    else:
        return text[(x - 1) // 2]


if __name__ == '__main__':
    # print("Example:")
    # print(middle('example'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert middle('example') == 'm'
    assert middle('test') == 'es'
    assert middle('very-very long sentence') == 'o'
    assert middle('I') == 'I'
    assert middle('no') == 'no'
    print("Coding complete? Click 'Check' to earn cool rewards!")
