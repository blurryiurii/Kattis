# https://open.kattis.com/problems/different

# difference between nonnegative integers
while 1:
    try:
        a, b = map(int, input().split())  # assuming two space-separated integers
        print(max(a-b, b-a))
    except:  # ValueError means we got EOF or newline in case of manual input
        break