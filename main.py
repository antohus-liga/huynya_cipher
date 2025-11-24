# ᚠᚡᚢᚣᚤᚥᚦᚧᚨᚩᚪᚫᚬᚭᚮᚯᚰᚱᚲᚳᚴᚵᚶᚷᚸᚹ ᛫᛬᛭ᛮᛯᛰ
# ☉☿♁♃♄♅♆♇⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⌖⌬⍟⍤⍥⍨⍩⍭ ∴∵⍪⸮‼-

"""
make options 1 - encode; 2 - decode.

first make a string that has all characters needed
then make a dictionary that has `cipher keys` as `dict keys`
and `encoded characters` as values (see the two examples above)
in a `for` loop, when DECODING, get the index of the current character
from the value of the current key character, return the character that has this
index in the human alphabet
when ENCODING, get the index of the current character in the human alphabet
then return the `encoded character` from the value of the current key character

after testing add error handling so it's more convenient to use
"""

print("1 - Encode")
print("2 - Decode\n")

human_alphabet = "abcdefghijklmnopqrstuvwxyz .,?!-"
encode_dict = {
    "a": "☉☿♁♃♄♅♆♇⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⌖⌬⍟⍤⍥⍨⍩⍭∴∵⍪⸮‼-",
    "b": "☿♁♃♄♅♆♇⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⌖⌬⍟⍤⍥⍨⍩⍭☉∴∵⍪⸮‼-",
    "c": "♁♃♄♅♆♇⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⌖⌬⍟⍤⍥⍨⍩⍭☉☿∴∵⍪⸮‼-",
    "d": "♃♄♅♆♇⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⌖⌬⍟⍤⍥⍨⍩⍭☉☿♁∴∵⍪⸮‼-",
    "e": "♄♅♆♇⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⌖⌬⍟⍤⍥⍨⍩⍭☉☿♁♃∴∵⍪⸮‼-",
    "f": "♅♆♇⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⌖⌬⍟⍤⍥⍨⍩⍭☉☿♁♃♄∴∵⍪⸮‼-",
    "g": "♆♇⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⌖⌬⍟⍤⍥⍨⍩⍭☉☿♁♃♄♅∴∵⍪⸮‼-",
    "h": "♇⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⌖⌬⍟⍤⍥⍨⍩⍭☉☿♁♃♄♅♆∴∵⍪⸮‼-",
    "i": "⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⌖⌬⍟⍤⍥⍨⍩⍭☉☿♁♃♄♅♆♇∴∵⍪⸮‼-",
    "j": "⚴⚵⚶⚷⚸⚹⚺⚻⚼⌖⌬⍟⍤⍥⍨⍩⍭☉☿♁♃♄♅♆♇⚳∴∵⍪⸮‼-",
    "k": "⚵⚶⚷⚸⚹⚺⚻⚼⌖⌬⍟⍤⍥⍨⍩⍭☉☿♁♃♄♅♆♇⚳⚴∴∵⍪⸮‼-",
    "l": "⚶⚷⚸⚹⚺⚻⚼⌖⌬⍟⍤⍥⍨⍩⍭☉☿♁♃♄♅♆♇⚳⚴⚵∴∵⍪⸮‼-",
    "m": "⚷⚸⚹⚺⚻⚼⌖⌬⍟⍤⍥⍨⍩⍭☉☿♁♃♄♅♆♇⚳⚴⚵⚶∴∵⍪⸮‼-",
    "n": "⚸⚹⚺⚻⚼⌖⌬⍟⍤⍥⍨⍩⍭☉☿♁♃♄♅♆♇⚳⚴⚵⚶⚷∴∵⍪⸮‼-",
    "o": "⚹⚺⚻⚼⌖⌬⍟⍤⍥⍨⍩⍭☉☿♁♃♄♅♆♇⚳⚴⚵⚶⚷⚸∴∵⍪⸮‼-",
    "p": "⚺⚻⚼⌖⌬⍟⍤⍥⍨⍩⍭☉☿♁♃♄♅♆♇⚳⚴⚵⚶⚷⚸⚹∴∵⍪⸮‼-",
    "q": "⚻⚼⌖⌬⍟⍤⍥⍨⍩⍭☉☿♁♃♄♅♆♇⚳⚴⚵⚶⚷⚸⚹⚺∴∵⍪⸮‼-",
    "r": "⚼⌖⌬⍟⍤⍥⍨⍩⍭☉☿♁♃♄♅♆♇⚳⚴⚵⚶⚷⚸⚹⚺⚻∴∵⍪⸮‼-",
    "s": "⌖⌬⍟⍤⍥⍨⍩⍭☉☿♁♃♄♅♆♇⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼∴∵⍪⸮‼-",
    "t": "⌬⍟⍤⍥⍨⍩⍭☉☿♁♃♄♅♆♇⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⌖∴∵⍪⸮‼-",
    "u": "⍟⍤⍥⍨⍩⍭☉☿♁♃♄♅♆♇⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⌖⌬∴∵⍪⸮‼-",
    "v": "⍤⍥⍨⍩⍭☉☿♁♃♄♅♆♇⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⌖⌬⍟∴∵⍪⸮‼-",
    "w": "⍥⍨⍩⍭☉☿♁♃♄♅♆♇⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⌖⌬⍟⍤∴∵⍪⸮‼-",
    "x": "⍨⍩⍭☉☿♁♃♄♅♆♇⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⌖⌬⍟⍤⍥∴∵⍪⸮‼-",
    "y": "⍩⍭☉☿♁♃♄♅♆♇⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⌖⌬⍟⍤⍥⍨∴∵⍪⸮‼-",
    "z": "⍭☉☿♁♃♄♅♆♇⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⌖⌬⍟⍤⍥⍨⍩∴∵⍪⸮‼-",
}

match input("Option: "):
    case "1":
        print("--------------")
        print("Encoding")

        key = input("Enter your key here: ")
        sentence = input("Enter your sentence here: ")
        encoded_sentece = ""

        k = 0
        for char in sentence:
            if k > len(key) - 1:
                k = 0

            key_char = key[k]
            i = human_alphabet.index(char)
            encoded_sentece += encode_dict[key_char][i]

            k += 1
        print(encoded_sentece)

    case "2":
        print("--------------")
        print("Decoding")

        key = input("Enter your key here: ")
        sentence = input("Enter your sentence here: ")
        decoded_sentece = ""

        k = 0
        for char in sentence:
            if k > len(key) - 1:
                k = 0

            key_char = key[k]
            i = encode_dict[key_char].index(char)
            decoded_sentece += human_alphabet[i]

            k += 1
        print(decoded_sentece)
