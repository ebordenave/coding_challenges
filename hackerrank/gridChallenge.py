def gridChallenge(grid):
    # Convert each row of the input grid from a string to a list of characters
    grid = [list(row) for row in grid]

    # Get the number of rows and columns in the grid
    r = len(grid)
    c = len(grid[0])

    # Sort each row of the grid in alphabetical order
    for i in range(r):
        grid[i].sort()

    # Check if each column of the grid is in non-decreasing order
    for j in range(c):
        for i in range(1, r):
            if not grid[i-1][j] <= grid[i][j]:
                # If the current element in the current row is less than the corresponding element in the previous row,
                # the function immediately returns "NO", indicating that the grid is not sorted properly.
                return "NO"

    # If the function has checked all columns and all rows without returning "NO", it returns "YES", indicating that the grid is sorted properly.
    return "YES"
