def gridChallenge(grid):
    idx = 0
    
    grid_size = len(grid[0])
    
    for s in grid:
        sorted_s = sorted(s)
        # print(sorted_s)
        # if sorted_s != s:
            # print(f" => {sorted_s},{s}")
    
    for idx in range(grid_size):
        for x, y in enumerate(grid[idx]):
            print(x,y)
        



grid  = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywua']

gridChallenge(grid)