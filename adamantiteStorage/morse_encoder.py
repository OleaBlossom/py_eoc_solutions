#!/usr/bin/env checkio --domain=epy run morse-encoder
MORSE = {'a': '.-', 'b': '-...', 'c': '-.-.',
         'd': '-..', 'e': '.', 'f': '..-.',
         'g': '--.', 'h': '....', 'i': '..',
         'j': '.---', 'k': '-.-', 'l': '.-..',
         'm': '--', 'n': '-.', 'o': '---',
         'p': '.--.', 'q': '--.-', 'r': '.-.',
         's': '...', 't': '-', 'u': '..-',
         'v': '...-', 'w': '.--', 'x': '-..-',
         'y': '-.--', 'z': '--..', '0': '-----',
         '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....', '6': '-....',
         '7': '--...', '8': '---..', '9': '----.'
         }
from pysnooper import snoop

@snoop()
def morse_encoder(text):
    sentence = []
    for word in text.lower().split(" "):
        encodedWord = []
        for t in word:
            encodedWord.append(MORSE[t])
        sentence.append(" ".join(encodedWord))

    return "   ".join(sentence)


if __name__ == '__main__':
    print("Example:")
    print(morse_encoder('some text'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_encoder("some text") == "... --- -- .   - . -..- -"
    assert morse_encoder("2018") == "..--- ----- .---- ---.."
    assert morse_encoder("It was a good day") == ".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"
    print("Coding complete? Click 'Check' to earn cool rewards!")
