# https://open.kattis.com/problems/modulararithmetic

while True:
    n, t = map(int, input().split())
    if (n, t) == (0, 0):
        break

    for i in range(t):
        a, op, b = input().split()
        a, b = int(a), int(b)
        if op == "+":
            print((a + b) % n)
        elif op == "-":
            print((a - b) % n)
        elif op == "/":
            try:
                print((a * pow(b, -1, n)) % n)
            except ValueError:
                print(-1)
        elif op == "*":
            print((a * b) % n)
        else:
            print("?")