r,c,n = map(int, input().split())

t = [(i+1, *map(lambda x: int(x)-1, input().split())) for i in range(n)]

def score(cur):
  return abs(ri-cur[1])+abs(ci-cur[2]) + cur[0]/10000000

first  = [[None]*c for _ in range(r)]
second = [[None]*c for _ in range(r)]
for ri in range(r):
  for ci in range(c):
    # t.sort(key=lambda cur: abs(ri-cur[1])+abs(ci-cur[2]) + cur[0]/10000000)
    close = t[0]
    for cur in t[1:]:
       if score(close) > score(cur):
          close = cur
    
    second2 = t[0]
    for cur in t[1:]:
       if score(second2) > score(cur) and cur != close:
          second2 = cur
    
    # print(t)
    # print(*(abs(ri-cur[1])+abs(ci-cur[2]) for cur in t))
    first[ri][ci]  = close
    second[ri][ci] = second2

for row in first:
    print(*(i for i,_,_ in row))
# print()
for row in second:
    print(*(i for i,_,_ in row))