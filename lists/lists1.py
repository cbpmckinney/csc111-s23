
mylist = [95, 65, 74, 32, 55, 100, 0]

sum = 0
num = len(mylist)
for i in range(num):
    sum = sum + mylist[i]
avg = sum / num

#print("Numbers: ", mylist, "Average: ", round(avg,2))

mylist2 = ["I", "LOVE", "YOU"]

#print(mylist2)

mylist3 = ["I", 5, "LOVE", mylist]
#print(mylist3)


for x in mylist3:
    print(x)

for i in range(len(mylist3)):
    print(mylist3[i])



