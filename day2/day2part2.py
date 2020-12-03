# Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
# 
# Given the same example list from above:
# 
# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to the new interpretation of the policies?


inFile = open("input.txt")
input = []
for i in inFile:
    input.append(i)
inFile.close()
validPasswords = 0

for x in range(len(input)):
    s = input[x].split()
    req = s[0].split("-")
    reqFirstPos = int(req[0])
    reqSecondPos = int(req[1])
    value = (s[1])[0]
    password = s[2]
        
    if (password[reqFirstPos-1] == value and password[reqSecondPos-1] != value) or (password[reqFirstPos-1] != value and password[reqSecondPos-1] == value):
        validPasswords+=1

print("valid passwords: ", validPasswords)