#to the game, each tile is seither a blank or contains a mine
#to the user, each tile is also either flagged, hidden, or revealed
#revealed tiles also have a number on them which means adjacent mines

#if player reveals a mine tile they lose
#if player reveals every blank tile they win
#on revealing a blank, reveal all other adjacent blanks recursively

#0=blank
#1=mine


def progressToString(progress):
    s = ("    0 1 2 3 4 5\n\n"+
        "0   ? ? ? ? ? ?\n"+
        "1   ? ? ? ? ? ?\n"+
        "2   ? ? ? ? ? ?\n"+
        "3   ? ? ? ? ? ?\n"+
        "4   ? ? ? ? ? ?\n"+
        "5   ? ? ? ? ? ?\n")
    return s


def countBombsNearby(grid,x,y):
    return 0


def reveal(grid, progress,x,y):
    #reveal this square
    progress[y][x] = countBombsNearby(grid, x,y)
    
    
        
def dig(grid,progress,x,y):
    
    spaceDug = grid[y][x]
    
    if spaceDug == 1:
        return False, True
    else:
        reveal(grid,progress,x,y)
    
    
    return False, False

#loop for whole game
while (True): 
    
    #generate grid
    g =[
        [0,0,0,0,1,0],
        [0,1,1,0,0,0],
        [0,0,0,0,0,0],
        [0,1,0,0,1,0],
        [0,0,0,1,0,0],
        [0,0,0,0,0,0],
    ]
    
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
       
    if won:
        input("\n\n\nYou Won. Press ENTER to restart ") 
    elif lost:
        input("\n\n\nYou Lost. Press ENTER to restart ") 

