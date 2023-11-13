"""Tom Schäfer, Erik Gladitz FPP WS23/24"""

def decrypt(text, shift):
    """ subtracts unicode shift onto text """
    plain = ""
    
    for char in text:
        if char.isalpha():
            plain += chr(ord(char) - (shift % 26))
        else:
            plain += char

    return plain

word_list = ["aus", "besteht", "erkannt", "Fehler", "funktioniert", "Hardware", "macht", 
             "nicht", "Problem", "Programm", "programmieren", "Python", "Software", "Spass", "Zeilen"]

cipher = "vxumxgssokxkt sginz Yvgyy"

for shift in range(26):
    plain = decrypt(cipher, shift)
    
    plain_words = plain.split()
    
    if all(word in word_list for word in plain_words):
        print(f"Verschiebungsfaktor {shift}: {plain}")