alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shiftChar(char, shift):
    pos = alphabet.find(char.upper())
    if pos == -1: return char
    newPos = (pos + shift) % len(alphabet)
    return alphabet[newPos].lower()

def shiftString(text, shift):
    newText = []
    for char in text:
        newText.append(shiftChar(char,shift))
    return ''.join(newText)

with open('data.txt', 'r') as myFile:
    data=myFile.read()

encrypted = shiftString(data, 5)
decrypted = shiftString(encrypted, -5)
print(encrypted)
print(decrypted)