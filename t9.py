n = int(input())

t9 = {
    "a": "2",
    "b": "22",
    "c": "222",
    "d": "3",
    "e": "33",
    "f": "333",
    "g": "4",
    "h": "44",
    "i": "444",
    "j": "5",
    "k": "55",
    "l": "555",
    "m": "6",
    "n": "66",
    "o": "666",
    "p": "7",
    "q": "77",
    "r": "777",
    "s": "7777",
    "t": "8",
    "u": "88",
    "v": "888",
    "w": "9",
    "x": "99",
    "y": "999",
    "z": "9999",
    " ": "0"
}

for i in range(1, n + 1):
    msg = input()
    print(f"Case #{i}: ")
    lm = len(msg)
    for i in range(lm):
        char = msg[i]
        print(t9[char], end="")
        if i == lm - 1:
            break
        if t9[msg[i + 1]][0] == t9[char][-1]:
            print(" ", end='')
    print()