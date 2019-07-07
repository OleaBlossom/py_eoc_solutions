#!/usr/bin/env checkio --domain=epy run reverse-roman-numerals
def reverse_roman(roman_string):

    #replace this for solution
    return 0

if __name__ == '__main__':
    print("Example:")
    print(reverse_roman('VI'))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');