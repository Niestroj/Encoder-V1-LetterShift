# I made this while incredibly tired. Forgive me, Cipher leets.
# This JUST SHIFTS LETTERS POSITION in the alphabet/codec.
# It is incredibly easy to reverse-engineer.
# I will make up for it by making some better encrypting scripts.
# EnSCRIPTion... lol

import os;
import random;

def decode():
    finalString = ""
    decodeThis = input("Enter Text to decode: ")
    decodeThis = decodeThis.lower()
    for i in decodeThis:
        if i == "a":     o = "y"
        elif i == "b":   o = "z"
        elif i == "c":   o = "a"
        elif i == "d":   o = "b"
        elif i == "e":   o = "c"
        elif i == "f":   o = "d"
        elif i == "g":   o = "e"
        elif i == "h":   o = "f"
        elif i == "i":   o = "g"
        elif i == "j":   o = "h"
        elif i == "k":   o = "i"
        elif i == "l":   o = "j"
        elif i == "m":   o = "k"
        elif i == "n":   o = "l"
        elif i == "o":   o = "m"
        elif i == "p":   o = "n"
        elif i == "q":   o = "o"
        elif i == "r":   o = "p"
        elif i == "s":   o = "q"
        elif i == "t":   o = "r"
        elif i == "u":   o = "s"
        elif i == "v":   o = "t"
        elif i == "w":   o = "u"
        elif i == "x":   o = "v"
        elif i == "y":   o = "w"
        elif i == "z":   o = "(e/x)"
        elif i == "ü":   o = "i"
        elif i == "α":   o = "o"
        elif i == "ä":   o = "u"
        elif i == "@":   o = "a"
        else: o = i
        finalString = finalString + o
    print(finalString)

def encode():
    encodeThis = input("Enter Text to encode: ")
    encodeThis = encodeThis.lower()
    finalString = ""
    for i in encodeThis:
        if i == "a":     o = "@"
        elif i == "b":     o = "d"
        elif i == "c":     o = "e"
        elif i == "d":     o = "f"
        elif i == "e":     o = "z"
        elif i == "f":     o = "h"
        elif i == "g":     o = "i"
        elif i == "h":     o = "j"
        elif i == "i":     o = "ü"
        elif i == "j":     o = "l"
        elif i == "k":     o = "m"
        elif i == "l":     o = "n"
        elif i == "m":     o = "o"
        elif i == "n":     o = "p"
        elif i == "o":     o = "α"
        elif i == "p":     o = "r"
        elif i == "q":     o = "s"
        elif i == "r":     o = "t"
        elif i == "s":     o = "u"
        elif i == "t":     o = "v"
        elif i == "u":     o = "ä"
        elif i == "v":     o = "x"
        elif i == "w":     o = "y"
        elif i == "x":     o = "z"
        elif i == "y":     o = "a"
        elif i == "z":     o = "b"
        elif i == " ":     o = " "
        elif i == ".":     o = "."
        else:   o = "█"
        
        smallBigText = random.randint(0, 1)
        if smallBigText == 0:   o.lower()
        else:                   o.upper()
        finalString = finalString + o
    print(finalString)
    

while True:
    choice = input("CHOOSE: DECODE OR ENCODE (1/2)")
    os.system(command="cls")
    if choice == "1":
        # This will be horrible. Im truly sorry but this is the only way to make
        #  sure you dont understand the text if you dont know my thoughts about it.
        print("Running Decoder...")
        decode()
    elif choice == "2":
        print("Running Encoder...")
        encode()