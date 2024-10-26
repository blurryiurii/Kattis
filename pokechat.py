s = input()
word = input()
key = {}
for i in range(len(s)):
    key[str(i).rjust(3, "0")] = s[i]

for i in range(len(s)):
    inx = i * 3
    print(key[inx:inx+2:])