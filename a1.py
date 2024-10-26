# not solved
n = int(input())
values = input().split()
big_side = 2 ** -3.0/4.0
small_side = 2 ** -5.0/4.0
_small = small_side
_big = big_side
need = 1
tape = 0

for i in range(2, n+1):
    need *= 2
    quantity = int(values[i])

    if i != 2 and i % 2 == 0:
        small_side /= 2
    elif i != 2:
        big_side /= 2

    if need < quantity:
        tape = tape + (small_side + big_side) * need * 2
        need -= quantity
        break
    else:
        tape = tape + (small_side + big_side) * quantity * 2
        need -= quantity

if need > 0:
    print("impossible")
else:
    print((tape - (_big + _small * 2) * 2) / 2.0)
