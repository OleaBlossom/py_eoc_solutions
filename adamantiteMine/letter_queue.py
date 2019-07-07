#!/usr/bin/env checkio --domain=epy run letter-queue
from collections import deque
# from pysnooper import snoop


# @snoop()
def letter_queue(commands):
    d = deque()
    for c in commands:
        if c == "POP":
            if len(d) > 0:
                d.popleft()
        else:
            d.append(c.split(" ")[1])
    result = "".join(d)
    return result


if __name__ == '__main__':
    print("Example:")
    print(letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
