#!/usr/bin/env checkio --domain=epy run binary-count
def binary_count(number: int) -> int:
    b = bin(number)
    c = str(b).count("1")
    return c


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(binary_count(4))

    assert binary_count(4) == 1
    assert binary_count(15) == 4
    assert binary_count(1) == 1
    assert binary_count(1022) == 9
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
