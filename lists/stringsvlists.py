
mystring = "ILOVEYOU"
mylist = [0,50,100,72]

print(hex(id(mystring)))
#mystring[0] = "Y"
mystring = mystring.replace("I","Y")
print(hex(id(mystring)))
#print(mystring[0])

print(mylist[3])

mylist[3] = "ILOVEYOU"

print(mylist)
