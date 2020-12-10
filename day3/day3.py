# You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).
# 
# The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:
# 
# From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.
# 
# The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:


y = 0
x = 0

inFile = open("input.txt")
lines = inFile.readlines()
mapWidth = len(lines[0].rstrip())
print(mapWidth)
treesHit = 0
notAtBottom = True
location = ""

while notAtBottom:
    
    # check if we're at the end of the map
    if x + 3 > mapWidth-1:
        #print("was at: ", x)
        x = (3 - ((mapWidth)-x))
        #print("now we're at: ", x)
    else:
        # right 3
        x+=3

    # down 1
    y+=1
    # check for bottom
    if y >= len(lines)-1:
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

print("trees hit: ", treesHit)

