n, k = map(int, input().split())

nums = set()
for i in range(n):
  nums.add(int(input()))

print(min(k, len(nums)))