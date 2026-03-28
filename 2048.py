# https://open.kattis.com/problems/2048

grid = list()
for _ in range(4):
    grid.append(list(map(int, input().split())))

direction = int(input())
if direction == 0:
    # left
    for i in range(4):
        for j in range(3):
            # find an available number to move to current cell
            neighbor = 0
            for k in range(j + 1, 4):
                if grid[i][k] != 0:
                    neighbor = grid[i][k]
                    break
            if grid[i][j] == 0 and neighbor != 0:  # move
                grid[i][j], grid[i][k] = neighbor, 0
            neighbor = 0
            for k in range(j + 1, 4):
                if grid[i][k] != 0:
                    neighbor = grid[i][k]
                    break
            if grid[i][j] == neighbor and grid[i][j] != 0:  # merge
                grid[i][j] *= 2
                grid[i][k] = 0
elif direction == 1:
    # up
    for i in range(4):  # i-th column
        for j in range(3):  # j-th row
            neighbor = 0
            for k in range(j + 1, 4):
                if grid[k][i] != 0:
                    neighbor = grid[k][i]
                    break
            if grid[j][i] == 0 and neighbor != 0:  # move
                grid[j][i], grid[k][i] = neighbor, 0
            neighbor = 0
            for k in range(j + 1, 4):
                if grid[k][i] != 0:
                    neighbor = grid[k][i]
                    break
            if grid[j][i] == neighbor and grid[j][i] != 0:  # merge
                grid[j][i] *= 2
                grid[k][i] = 0
        
elif direction == 2:
    # right
    for i in range(4):
        for j in range(3, 0, -1):
            # find an available number to move to current cell
            neighbor = 0
            for k in range(j - 1, -1, -1):
                if grid[i][k] != 0:
                    neighbor = grid[i][k]
                    break
            if grid[i][j] == 0 and neighbor != 0:  # move
                grid[i][j], grid[i][k] = neighbor, 0
            neighbor = 0
            for k in range(j - 1, -1, -1):
                if grid[i][k] != 0:
                    neighbor = grid[i][k]
                    break
            if grid[i][j] == neighbor and grid[i][j] != 0:  # merge
                grid[i][j] *= 2
                grid[i][k] = 0
else:  # direction = 3
    # down
    for i in range(4):  # i-th column
        for j in range(3, 0, -1):  # j-th row
            neighbor = 0
            for k in range(j - 1, -1, -1):
                if grid[k][i] != 0:
                    neighbor = grid[k][i]
                    break
            if grid[j][i] == 0 and neighbor != 0:  # move
                grid[j][i], grid[k][i] = neighbor, 0
            neighbor = 0
            for k in range(j - 1, -1, -1):
                if grid[k][i] != 0:
                    neighbor = grid[k][i]
                    break
            if grid[j][i] == neighbor and grid[j][i] != 0:  # merge
                grid[j][i] *= 2
                grid[k][i] = 0

for i in range(4):
    print(" ".join(map(str, grid[i])))