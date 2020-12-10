# --- Part Two ---
# Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.
# 
# Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:
# 
# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
# In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.


slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
multiplied = 1

inFile = open("input.txt")
lines = inFile.readlines()
mapWidth = len(lines[0].rstrip())
inFile.close()


for s in slopes:
    y = 0
    x = 0
    treesHit = 0
    notAtBottom = True
    location = ""
    while notAtBottom:
        
        # check if we're at the end of the map
        if x + s[0] > mapWidth-1:
            #print("was at: ", x)
            x = (s[0] - ((mapWidth)-x))
            #print("now we're at: ", x)
        else:
            # to the right
            x+=s[0]

        # down
        y+=s[1]
        # check for bottom
        if y >= len(lines)-s[1]:
            notAtBottom = False
        piece = list(lines[y].rstrip())
        location = piece[x]
        #print("location:", x+1, ",", y+1)
        if location == '#':
            piece[x] = "X" 
            #print(str(y)+"".join(piece))
            treesHit+=1
        else:
            piece[x] = "O" 
            #print(str(y)+"".join(piece))

    print("slope: ", s, "trees hit: ", treesHit)
    multiplied*=treesHit

print("multiplied together: ", multiplied)