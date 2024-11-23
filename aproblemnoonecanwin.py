# https://open.kattis.com/problems/aprizenoonecanwin

n, x = map(int, input().split())
nums = list(map(int, input().split()))


nums.sort()

for i, num in enumerate(nums):
    if i + 1 == n or num + nums[i + 1] > x:
        print(i + 1)
        break