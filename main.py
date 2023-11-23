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
    bomb = False


    while (not won and not bomb):
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
        