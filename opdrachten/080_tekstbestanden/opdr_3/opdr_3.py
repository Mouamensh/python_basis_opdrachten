# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:



def encrypt(tekst):
    versleuteld = ""
    for letter in tekst:
        if 'a' <= letter <= 'z':
            versleuteld += chr(((ord(letter) - ord('a') + 5) % 26) + ord('a'))
        elif 'A' <= letter <= 'Z':
            versleuteld += chr(((ord(letter) - ord('A') + 5) % 26) + ord('A'))
        else:
            versleuteld += letter
    return versleuteld

def decrypt(versleuteld):
    ontsleuteld = ""
    for letter in versleuteld:
        if 'a' <= letter <= 'z':
            ontsleuteld += chr(((ord(letter) - ord('a') - 5) % 26) + ord('a'))
        elif 'A' <= letter <= 'Z':
            ontsleuteld += chr(((ord(letter) - ord('A') - 5) % 26) + ord('A'))
        else:
            ontsleuteld += letter
    return ontsleuteld

tekst = input("Geef de tekst die je wilt encrypten: ")
versleuteld = encrypt(tekst)
print(versleuteld)
