# https://open.kattis.com/problems/inflation2
dishes = int(input())
prices = list(map(int, input().split()))
days = int(input())

pricesum = sum(prices)

for i in range(days):
    line = input().split()

    if line[0] == "INFLATION":
        prices = list(map(lambda x: x + int(line[1]), prices))
        pricesum += int(line[1]) * dishes
    elif line[0] == "SET":
        arg1 = int(line[1])
        arg2 = int(line[2])
        for i in range(dishes):
            if prices[i] == arg1:
                prices[i] = arg2
        pricesum = sum(prices)
    print(pricesum)