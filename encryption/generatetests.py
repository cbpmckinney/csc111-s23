import random
import McKinneyEncryptionLibrary as MCKLIB

listfile = open("listofwords.txt", "r")

ListOfWords = []

for line in listfile:
    ListOfWords.append(line.replace("\n", ""))

listfile.close()

caesarfile = open("caesar.txt", "w")

for i in range(100):
    message = ""
    # This part generates a string of random words
    for j in range(random.randrange(2, 5, 1)):
        randword = ListOfWords[random.randrange(len(ListOfWords))]
        message = message + randword
    shift = random.randrange(1, 26, 1)
    scrambled = MCKLIB.CaesarEncrypt(message, shift)

    caesarfile.write(message + "," + str(shift) + "," + scrambled + "\n")
    assert MCKLIB.CaesarDecrypt(scrambled, shift) == message

caesarfile.close()

# Generate EvilCaesar Test Cases

evilcaesarfile = open("evilcaesar.txt", "w")

for i in range(100):
    message = ""
    # This part generates a string of random words
    for j in range(random.randrange(2, 5, 1)):
        randword = ListOfWords[random.randrange(len(ListOfWords))]
        message = message + randword
    shift1 = random.randrange(1, 26, 1)
    shift2 = random.randrange(1, 26, 1)
    scrambled = MCKLIB.EvilCaesarEncrypt(message, shift1, shift2)

    evilcaesarfile.write(message + "," + str(shift1) +
                         "," + str(shift2) + "," + scrambled + "\n")
    assert MCKLIB.EvilCaesarDecrypt(scrambled, shift1, shift2) == message

evilcaesarfile.close()


# Generate Vigenere Test Cases

vigenerefile = open("vigenere.txt", "w")

for i in range(100):
    message = ""
    # This part generates a string of random words
    for j in range(random.randrange(2, 5, 1)):
        randword = ListOfWords[random.randrange(len(ListOfWords))]
        message = message + randword
    key = str(ListOfWords[random.randrange(len(ListOfWords))])
    scrambled = MCKLIB.VigenereEncrypt(message, key)

    vigenerefile.write(message + "," + key + "," + scrambled + "\n")
    assert MCKLIB.VigenereDecrypt(scrambled, key) == message

vigenerefile.close()
