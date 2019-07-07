#!/usr/bin/env checkio --domain=epy run unlucky-days
def unlucky_days(year: int) -> int:
    return 0

if __name__ == '__main__':
    print("Example:")
    print(unlucky_days(2015))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert unlucky_days(2015) == 3, "First - 2015"
    assert unlucky_days(1986) == 1, "Second - 1986"
    print("Coding complete? Click 'Check' to earn cool rewards!")
