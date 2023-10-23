def caesar_decrypt(text, shift):
    decrypted_text = ""
    
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            elif char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        else:
            decrypted_char = char

        decrypted_text += decrypted_char

    return decrypted_text

# Gegebene Wortliste
word_list = [
    "aus", "besteht", "erkannt", "Fehler", "funktioniert", "Hardware", "macht",
    "nicht", "Problem", "Programm", "programmieren", "Python", "Software", "Spaß", "Zeilen"
]

# Verschlüsselter Text
encrypted_text = "vxumxgssokxkt sginz yvgyy"

# Durch alle möglichen Verschiebungen iterieren
for shift in range(26):
    decrypted_text = caesar_decrypt(encrypted_text, shift)
    
    # Die Wörter im entschlüsselten Text ermitteln
    decrypted_words = decrypted_text.split()
    
    # Überprüfen, ob alle Wörter im entschlüsselten Text in der Wortliste sind
    if all(word.lower() in word_list for word in decrypted_words):
        print(f"Verschiebungsfaktor {shift}: {decrypted_text}")
