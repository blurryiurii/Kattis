input()
opuses = list(map(int, input().split()))  # 8, 2, 4, 2
people = [i for i in range(1, len(opuses) + 1)] # 1, 2, 3...

inx = 0
while len(people) > 1:
    inx = (inx + opuses[inx] - 1) % len(people)
    opuses.pop(inx)
    people.pop(inx)
    inx %= len(people)

print(people[0])
