#to the game, each tile is seither a blank or contains a mine
#to the user, each tile is also either flagged, hidden, or revealed
#revealed tiles also have a number on them which means adjacent mines

#if player reveals a mine tile they lose
#if player reveals every blank tile they win
#on revealing a blank, reveal all other adjacent blanks recursively

#0=blank
#1=mine
  
#loop for whole game
while (True): 
    
    def dig(x,y):
        
        spaceDug = grid[y][x]
        
        if spaceDug == 1:
            return False, True
        
        
        return False, False
    
    #generate grid
    grid =[
        [0,0,0,0,1,0],
        [0,1,1,0,0,0],
        [0,0,0,0,0,0],
        [0,1,0,0,1,0],
        [0,0,0,1,0,0],
        [0,0,0,0,0,0],
    ]
    
    won = False
    lost = False


    while (not won and not lost):
        print(
        "    0 1 2 3 4 5\n\n"+
        "0   ? ? ? ? ? ?\n"+
        "1   ? ? ? ? ? ?\n"+
        "2   ? ? ? ? ? ?\n"+
        "3   ? ? ? ? ? ?\n"+
        "4   ? ? ? ? ? ?\n"+
        "5   ? ? ? ? ? ?\n"
        )
        x = int(input("dig x(column): "))
        y = int(input("dig y(row): "))
        
        won, lost = dig(x,y)
       
    if won:
        input("\n\n\nYou Won. Press ENTER to restart ") 
    elif lost:
        input("\n\n\nYou Lost. Press ENTER to restart ") 

        
        