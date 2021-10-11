emptygrid = '|  |  |  |  |  |  |  |  |  |'
across =    '\n----------------------------'
row = emptygrid + across

pos1 = '| O|  |  |  |  |  |  |  |  |'+across
pos2 = '|  | O|  |  |  |  |  |  |  |'+across
pos3 = '|  |  | O|  |  |  |  |  |  |'+across
pos4 = '|  |  |  | O|  |  |  |  |  |'+across
pos9 = '|  |  |  |  |  |  |  |  | O|'+across
pos6 = '|  |  |  |  |  | O|  |  |  |'+across
pos7 = '|  |  |  |  |  |  | O|  |  |'+across
pos8 = '|  |  |  |  |  |  |  | O|  |'+across
pos5 = '|  |  |  |  | O|  |  |  |  |'+across

x = [None,pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9]

xpos = 5
ypos = 5

#originalgrid = across+row+row+row+row+pos5+row+row+row+row
originalgrid = [across,row,row,row,row,pos5,row,row,row,row]


grid = originalgrid
#position of y coord is same as grid[]

def drawgrid():
    for i in grid:
        print(i)
drawgrid()

while True:
    movement = input().strip().lower()
    if movement == 'z':
        break
    elif movement == 'w':
        if ypos == 1:
            print('At world border!')
        else:
            grid[ypos-1]=grid[ypos]
            grid[ypos] = row
            ypos = ypos-1
            drawgrid()
    elif movement == 's':
        if ypos == 9:
            print('At world border!')
        else:
            grid[ypos+1]=grid[ypos]
            grid[ypos] = row
            ypos = ypos+1
            drawgrid()
    elif movement == 'a':
        if xpos == 1:
            print('At world border!')
        else:
            grid[ypos ] =x[xpos-1]
            xpos = xpos-1
            drawgrid()
    elif movement == 'd':
        if xpos == 9:
            print('At world border!')
        else:
            grid[ypos ] =x[xpos+1]
            xpos = xpos+1
            drawgrid()
