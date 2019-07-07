#!/usr/bin/env checkio --domain=epy run end-of-other
def end_of_other(words_set):
    for x in words_set:
        for y in words_set:
            if x != y and (x.endswith(y) or y.endswith(x)):
                return True
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(end_of_other({"hello", "lo", "he"}))

    assert end_of_other({"hello", "lo", "he"}) == True, "helLO"
    assert end_of_other({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert end_of_other({"walk", "duckwalk"}) == True, "duck to walk"
    assert end_of_other({"one"}) == False, "Only One"
    assert end_of_other({"helicopter", "li", "he"}) == False, "Only end"
    print("Done! Time to check!")
