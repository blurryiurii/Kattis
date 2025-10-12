n, m = map(int, input().split())
from collections import defaultdict
deg = defaultdict(set)
for i in range(m):
  a, b = map(int, input().split())
  deg[a].add(b)
  deg[b].add(a)

print(deg)
for k in deg:
  curr = len(deg[k])
  for j in deg[k]:
    if len(deg[j]) != curr:
      print(-1)
      print(k, j, curr, len(deg[j]))

for i in range(n):
  for j in range(n):
    print(10000 / len(deg[i+1]), end=" ")
  print()