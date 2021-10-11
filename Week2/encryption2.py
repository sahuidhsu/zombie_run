plaintext = input("Plaintext:")
cipherText = ""
plaintextPosition = 0
while plaintextPosition < len(plaintext):
    plaintextChar = plaintext[plaintextPosition]
    asciiValue = ord(plaintextChar)
    asciiValue -= 3
    cipherText = cipherText + chr(asciiValue)
    plaintextPosition += 1
print(cipherText)