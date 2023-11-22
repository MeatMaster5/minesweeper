#to the game, each tile is seither a blank or contains a mine

#to the user, each tile is also either flagged, hidden, or revealed
#revealed tiles also have a number on them which means adjacent mines

#if player reveals a mine tile they lose
#if player reveals every blank tile they win
#on revealing a blank, reveal all other adjacent blanks recursively

#0=blank
#1=mine
grid =[
    [0,0,0,0,1,0],
    [0,1,1,0,0,0],
    [0,0,0,0,0,0],
    [0,1,0,0,1,0],
    [0,0,0,1,0,0],
    [0,0,0,0,0,0],
]
