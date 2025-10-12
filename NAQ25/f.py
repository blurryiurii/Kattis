n, k = map(int, input().split())
nums = list()
for i in range(n):
  nums.append(int(input()))

from itertools import combinations

perms = combinations(nums, k)
# print(perms)

from functools import lru_cache

@lru_cache()
def calc(avg, p):
  return (avg - p) ** 2

# step 1
sq_devs = list()
best = float("inf")
for perm in perms:
  avg = sum(perm) / k
  s = 0
  for p in perm:
    s += calc(avg, p)
    if s > best:
      break
  else:
    sq_devs.append(s)

print(min(sq_devs))