def UpperCase(string): # accept a string, upper-case it, and return
    result = ""
    for i in range(len(string)):
        if (string[i] >= 'a') and (string[i] <= 'z'):
            result = result + chr(ord(string[i])-32)
        else:
            result = result + string[i]    
    return result


string1 = "Wabash Always Fights!"
print(string1.upper())
print(UpperCase(string1))