"""Tom Schäfer, Erik Gladitz FPP WS23/24"""


def encrypt(plain, shift):
    """ adds unicode shift onto text """

    cipher = ""

    for char in plain:
        cipher += chr(ord(char) + (shift % 26))

    return cipher


def input():
    """ read & check if input (origin-text + shift-value) is applicable for ceasar-algorithm """

    while True:
        plain = input("Plaintext eingeben: ")
        if plain.isalpha():
            break
        else:
            print('Bitte gib nur Buchstaben ein!')

    while True:
        shift = input("Verschiebungsfaktor eingeben: ")
        if shift.isnumeric():
            shift = int(shift)
            break
        else:
            print('Bitte gib eine ganze Zahl ein!')
    return plain, shift


if __name__ == "__main__":
    cipher = encrypt(input())
    print("Ciphertext:", cipher)