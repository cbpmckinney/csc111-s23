import random


def SubstitutionEncrypt(plainstring, alphabet):
    encryptedstring = ""
    plainalphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictlist = []
    for i in range(0,26):
        dictlist.append((plainalphabet[i], alphabet[i]))

    dictionary = dict(dictlist)

    for i in range(len(plainstring)):
        encryptedstring = encryptedstring + dictionary[plainstring[i]]

    return encryptedstring

mystring = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
myalphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
newalphabet = ""

for i in range(0,26):
    randomnumber = random.randrange(0,len(myalphabet))
    newalphabet = newalphabet + myalphabet[randomnumber]
    myalphabet = myalphabet.replace(myalphabet[randomnumber],"")

print("Old Alphabet: \t" + myalphabet)
print("New Alphabet: \t" + newalphabet)


newstring = SubstitutionEncrypt(mystring, newalphabet)

print("Plain text: \t" + mystring)
print("Cipher text: \t" + newstring)



