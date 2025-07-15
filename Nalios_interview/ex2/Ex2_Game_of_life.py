# Ex 2 : Game of Life
# I have to return the grid after 5 iterrations.
#  
#Rules of a game of life :
# For a space that is populated:
#   Each cell with one or no neighbors dies, as if by solitude.
#   Each cell with four or more neighbors dies, as if by overpopulation.
#   Each cell with two or three neighbors survives.
# For a space that is empty or unpopulated:
#   Each cell with three neighbors becomes populated.

#logic of my solution:
# The grid is represented as a 2D list and i'll apply every rule to each cell in the grid.

def Game_Start(grid):
    for turn in range(5):  # Run the game for 5 turns
        new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]  # Create a new grid for the next state of the same dimension as the original grid
        for line in range(len(grid)):
            for col in range(len(grid[0])):
                alive_neighbors = 0
                for dx in [-1, 0, 1]: 
                    for dy in [-1, 0, 1]:  
                        if dx == 0 and dy == 0:
                            continue  # Skip the cell itself, can't count itself as a neighbor after all
                        neighbor_x = line + dx
                        neighbor_y = col + dy
                        # Check if the neighbor is within bounds of the grid
                        if 0 <= neighbor_x < len(grid) and 0 <= neighbor_y < len(grid[0]):
                            alive_neighbors += grid[neighbor_x][neighbor_y]
                if grid[line][col] == 1:  # Cell is alive
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_grid[line][col] = 0  # Cell dies
                    else:
                        new_grid[line][col] = 1  # Cell survives
                else:  # Cell is dead
                    if alive_neighbors == 3:
                        new_grid[line][col] = 1  # Cell created 
        grid = new_grid  # Update the grid to the new state

        # Bonus: output the grid in html
        # I went for a table element to keep the matrix structure of the grid.
        # i just iterate through the grid and print each cell in a table row.
        # This will create a simple HTML file with the output.

        with open("Ex2output.html", "w") as f:
            f.write("<table>")
            for row in grid:
                f.write("<tr>")
                for cell in row:
                    f.write(f"<td>{cell}</td>")
                f.write("</tr>")
            f.write("</table>")

    return grid

# Tests of the game :

test_grid1 = [
    [0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0]
]
test_grid2 = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1]
]

# result_grid = Game_Start(test_grid1)
# for row in result_grid:
#     print(row)  
# print ("\n")
result_grid = Game_Start(test_grid2)
for row in result_grid:
    print(row)  