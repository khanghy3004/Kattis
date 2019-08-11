new_alphabet = {
    "A": "@",
    "B": "8",
    "C": "(",
    "D": "|)",
    "E": "3",
    "F": "#",
    "G": "6",
    "H": "[-]",
    "I": "|",
    "J": "_|",
    "K": "|<",
    "L": "1",
    "M": "[]\\/[]",
    "N": "[]\\[]",
    "O": "0",
    "P": "|D",
    "Q": "(,)",
    "R": "|Z",
    "S": "$",
    "T": "']['",
    "U": "|_|",
    "V": "\\/",
    "W": "\\/\\/",
    "X": "}{",
    "Y": "`/",
    "Z": "2"
}


def change(s):
    o = ord(s)
    if 97 <= o <= 122:
        return new_alphabet[chr(o - 32)]
    if 65 <= o <= 90:
        return new_alphabet[s]
    return s

for s in input():
    print(change(s), end='')