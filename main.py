#to the game, each tile is seither a blank or contains a mine
#to the user, each tile is also either flagged, hidden, or revealed
#revealed tiles also have a number on them which means adjacent mines

#if player reveals a mine tile they lose
#if player reveals every blank tile they win
#on revealing a blank, reveal all other adjacent blanks recursively

#0=blank
#1=mine


#------------------------
# grid reveal needs to reveal adjacent squares idk how to make it do that
# also add win condition
#------------------------

def progressToString(progress):

    s = "    "
    size = len(progress)
    for i in range(size):
        s+=str(i)+" "
    s+="\n\n"
    for row in range(size):
        s+=str(row)+"   "
        
        for column in range(size):
            val = progress[row][column] 
            if val == -1:
                s+="□ "
            elif val == -2:
                s+="X "
            else:
                s+=str(val)+" "
        s+="\n"
    return s

def getBounds(grid,x,y):
    left = x-1
    right = x+2
    if x < 1:
        left = 0
    if x > len(grid)-2:
        right = len(grid)-1
    below = y-1
    up = y+2
    if y < 1:
        below = 0
    if y>len(grid)-2:
        up=len(grid)-1
    return left,right,below,up

def countBombsNearby(grid,progress,x,y):
    count = 0
    left,right,below,up = getBounds(grid,x,y)
    for column in range(left,right):
        for row in range(below,up):
            if row == y and column == x:
                continue
            print(row,column)
            if grid[row][column] == 1:
                count+=1
            
    return count


def reveal(grid, progress,x,y):
    #reveal this square
    if grid[y][x] == 1:
        progress[y][x] = -2
    else:
        bombs = countBombsNearby(grid,progress,x,y)
        progress[y][x] = bombs
        
    
        
def dig(grid,progress,x,y):
    
    spaceDug = grid[y][x]
    
    reveal(grid,progress,x,y)
    
    if spaceDug == 1:
        return False, True
    else:
        return False, False

#loop for whole game
while (True): 
    
    #generate grid
    g =[
        [0,0,0,0,1,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,1,0,0,1,0],
        [0,0,0,1,0,0],
        [0,0,0,0,0,0],
    ]
    
    # -2 = bomb
    # -1 = not revealed
    # 0-8  = number of bombs adjacent
    prog=[
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
    ]
    
    won = False
    lost = False


    while (not won and not lost):
        print(progressToString(prog))
        x = int(input("dig x(column): "))
        y = int(input("dig y(row): "))
        
        won, lost = dig(g,prog,x,y)
       
    print(progressToString(prog))
    if won:
        input("You Won. Press ENTER to restart ") 
    elif lost:
        input("You Lost. Press ENTER to restart ") 

