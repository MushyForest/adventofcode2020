
# --- Part Two ---
# The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.
# 
# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.
# 
# In your expense report, what is the product of the three entries that sum to 2020?

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
        for z in range(y, lenInput):
            count+=1
            a = int(input[x])
            b = int(input[y])
            c = int(input[z])
            if a + b + c == targetSum:
                print("found: ", a, ", ", b, ", ", c)
                print("multiplied for: ", a*b*c)

print("total tries: ", count)