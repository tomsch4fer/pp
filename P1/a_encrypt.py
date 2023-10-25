"""Tom Schäfer, Erik Gladitz FPP WS23/24"""


def encrypt(plain, shift):
    cipher = ""

    for char in plain:
        cipher += chr(ord(char) + (shift % 26))

    return cipher

# check if input is applicable for ceasar-algorithm
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

cipher = encrypt(plain, shift)
print("Ciphertext:", cipher)