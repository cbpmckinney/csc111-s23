def caesar(thestring, shift):
    message = ""

    for i in range(len(thestring)):
        letter = chr(((ord(thestring[i]) - 65 + shift) % 26) + 65)
        message = message + letter

    return message


mystring = "ILOVEYOU"
print("Original Text: ", mystring)
print("Cipher Text:   ", caesar(mystring, -13))

ciphertext = "VYBIRLBH"
print("------------------------------")

for i in range(1,26):
    print("Key: ", i , "\t", caesar(ciphertext, -i))



