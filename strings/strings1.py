def mystringlength(mystring):
    counter = 0
    for i in mystring:
        counter += 1    
    return counter

string1 = "Hello"
string2 = "World"
string3 = "Wabash"

print(len(string1))
print(mystringlength(string1))


#for i in range(len(string1)):
#    print(string1[i])
