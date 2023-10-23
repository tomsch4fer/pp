def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            elif char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_char = char

        encrypted_text += encrypted_char

    return encrypted_text

# Eingabe von Text und Verschiebungsfaktor durch den Benutzer
text = input("Geben Sie den zu verschlüsselnden Text ein: ")
shift = int(input("Geben Sie den Verschiebungsfaktor ein (eine ganze Zahl): "))

# Verschlüsselung des Textes
encrypted_text = encrypt(text, shift)

# Ausgabe des verschlüsselten Textes
print("Verschlüsselter Text:", encrypted_text)
