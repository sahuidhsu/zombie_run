def encryption():
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

def decryption():
    plaintext = input("Ciphertext:")
    cipherText = ""
    plaintextPosition = 0
    while plaintextPosition < len(plaintext):
        plaintextChar = plaintext[plaintextPosition]
        asciiValue = ord(plaintextChar)
        asciiValue += 3
        cipherText = cipherText + chr(asciiValue)
        plaintextPosition += 1
    print(cipherText)

again = True
while again == True:
    print("Which do you want?")
    print("Enter the following instruction:")
    enter = int(input("1 for encryption  2 for decryption:"))
    while (enter != 1) and (enter != 2):
        print("Seems like your enter is invalid!")
        print("Please try again!")
        enter = int(input("1 for encryption  2 for decryption:"))
    if enter == 1:
        encryption()
    if enter == 2:
        decryption()
    print("Well Done! Do you wish to continually run the program?")
    enter = input("Y for yes  N for no:")
    while (enter != "Y") and (enter != "N"):
        print("Seems like your enter is invalid!")
        print("Please try again!")
        enter = input("Y for yes  N for no:")
    if enter == "Y":
        again = True
    else:
        again = False
