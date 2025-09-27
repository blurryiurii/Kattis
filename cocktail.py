n, t = map(int, input().split())

potions = list()
for i in range(n):
    potions.append(int(input()))
potions.sort()

valid = True
for i, potion in enumerate(potions):
    if (potion <= (i * t)):
        print("NO")
        break
else:
    print("YES")