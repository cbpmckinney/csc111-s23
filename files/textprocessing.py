
inputtext = open("iliad2.txt","r")
outputtext = open("output.txt","w")

listofwords = []

for line in inputtext:
    thislinewords = line.split()
    for word in thislinewords:
        word = word.replace(",","")
        word = word.replace(";","")
        word = word.replace(".","")
        word = word.replace("!","")
        word = word.replace(":","")
        word = word.replace("?","")
        word = word.replace("(","")
        word = word.replace(")","")
        listofwords.append(word)

#print(listofwords)
print("There are " + str(len(listofwords)) + " words")

dedupedlist = []

for word in listofwords:
    if word not in dedupedlist:
        dedupedlist.append(word)

print(len(dedupedlist))

dedupedlist.sort()

wordcountlist = []

for word in dedupedlist:
    count = listofwords.count(word)
    wordcountlist.append([word, count])
    outputtext.write(word + ": " + str(count) + "\n")

#print(dedupedlist)
print(wordcountlist)


inputtext.close()
outputtext.close()
