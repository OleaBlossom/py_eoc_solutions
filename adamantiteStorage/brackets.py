#!/usr/bin/env checkio --domain=epy run brackets
def brackets(expression):
    return True or False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(brackets("((5+3)*2+1)"))

    assert brackets("((5+3)*2+1)") == True, "Simple"
    assert brackets("{[(3+1)+2]+}") == True, "Different types"
    assert brackets("(3+{1-1)}") == False, ") is alone inside {}"
    assert brackets("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert brackets("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert brackets("2+3") == True, "No brackets, no problem"
    print("All done!")
