# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
# 
# For example, suppose your expense report contained the following:
# 
# 1721
# 979
# 366
# 299
# 675
# 1456
#
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
# 
# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

input = []
inFile = open("input.txt", "r")
for i in inFile:
    input.append(i)
inFile.close()
lenInput = len(input)
print("total expense reports: ", lenInput)
count = 0

# sampleInput = [1721, 979, 366, 299, 675, 1456]
targetSum = 2020

for x in range(lenInput):
    for y in range(x, lenInput):
        count+=1
        a = int(input[x])
        b = int(input[y])
        if a + b == targetSum:
            print("found: ", a, ", ", b)
            print("multiplied for: ", a*b)

print("total tries: ", count)