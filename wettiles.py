# not finished


test_cases = []
file = open("input.txt", "r")

while (n_case := file.readline().strip()) != "-1":
    # Parse state data
    x_coord, y_coord, t, l, w = n_case.split()
    t, l, w = int(t), int(l), int(w)

    leaks = []
    while l != len(leaks):  # while we haven't gotten all leak coords
        # parse a line of leak coords
        l_coords = file.readline().split()
        # get pairs of integers and add them to leaks[]
        for x, y in zip(l_coords[0::2], l_coords[1::2]):
            leaks.append((int(x), int(y)))

    walls = []
    while w != len(walls):  # while we haven't gotten all wall coords
        # parse a line of wall coords
        w_coords = file.readline().split()
        while w_coords:
            walls.append([int(w_coords[x]) - 1 for x in range(4)])
            del(w_coords[0:4])

    data = {
        "coords": (int(x_coord), int(y_coord)),
        "time": t,
        "leaks": leaks,
        "walls": walls
    }
    test_cases.append(data)
file.close()

for test_case in test_cases:
    x, y = test_case["coords"]
    arr = [[" " for _ in range(x)] for _ in range(y)]

    # Water leak placements
    for leak in test_case["leaks"]:
        x_coord, y_coord = leak
        print(leak)
        arr[y_coord][x_coord] = "L"

    # Wall placements
    """for wall in test_case["walls"]:
        print("WALL", wall)
        sx, sy, ex, ey = wall
        
        # Make starting vars less than end vars
        if sx > ex:
            sx, ex = ex, sx
        if sy > ey:
            sy, ey = ey, sy

        if sy == ey:  # Horizontal
            for x_coord in range(sx, ex + 1):
                arr[sy][x_coord] = "#"
        elif sx == ex:  # Vertical
            for y_coord in range(sy, ey + 1):
                arr[y_coord][sx] = "#"
        else:  # Diagonal
            for i in range(ey - sy + 1):
                arr[y - (sy+i)][x - (sx+x)] = "#" """

    print("_" * 14)
    for i in range(len(arr)):
        print("|", end="")
        for j in range(len(arr[0])):
            print("".join(arr[y - j - 1][i]), end="")
        print("|")
    print("_" * 14)

    exit()
