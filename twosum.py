from math import sqrt

# input
arr = [input().split(), input().split(), input().split()]
# convert to integers
for i in range(3):
    for j in range(3):
        arr[i][j] = int(arr[i][j])


# locate x, y of n coords given n
def locate(arr, n):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == n:
                return i, j


# start at number 1
sum = 0
x, y = locate(arr, 1)

# loop through nums 2...9
for n in range(2, 10):
    new_x, new_y = locate(arr, n)
    sum += sqrt(abs(new_x - x) ** 2 + abs(new_y - y) ** 2)
    x, y = new_x, new_y

print(sum)