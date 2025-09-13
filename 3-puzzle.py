# Iurii Chmykhun

# There's a reason 2x2 rotation puzzles don't exist...

# seamlessly convert input to 1d array
# [top_left, top_right, bottom_left, bottom_right]
nums = list(input())
nums.extend(list(input()))
# print(nums)

def rotate(l: list):
    dash = l.index('-')  # index of dash
    # rotate dash counterclockwise
    if dash == 0:
        l[0], l[2] = l[2], l[0]
    elif dash == 1:  # horizontal moves
        l[1], l[0] = l[0], l[1]
    elif dash == 2:
        l[2], l[3] = l[3], l[2]
    elif dash == 3:
        l[3], l[1] = l[1], l[3]
    return l


c = 0
while c < 67:
    if nums[:3] == ["1", "2", "3"]:
        break
    nums = rotate(nums)
    c += 1
else:
    exit("failed")
print(c % 24)  # mod 24: in case rotating dash clockwise would've been more optimal

# wrong answer result in test case #8