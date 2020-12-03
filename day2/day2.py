# To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.
# 
# For example, suppose you have the following list:
# 
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
# 
# In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.
# 
# How many passwords are valid according to their policies?

inFile = open("input.txt")
input = []
for i in inFile:
    input.append(i)
inFile.close()
validPasswords = 0

for x in range(len(input)):
    s = input[x].split()
    req = s[0].split("-")
    reqMin = int(req[0])
    reqMax = int(req[1])
    value = (s[1])[0]
    password = s[2]
    
    #print("v: ", reqMin, reqMax, value, password)
    valueCount = 0
    for letter in password:
        if letter == value:
            valueCount+=1
        
    if valueCount >= reqMin and valueCount <= reqMax:
        validPasswords+=1

print("valid passwords: ", validPasswords)



