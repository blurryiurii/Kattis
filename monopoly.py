from collections import Counter

nums = []
for i in range(1, 7):
    for j in range(1, 7):
        nums.append(i+j)
nums = Counter(nums)
print(nums[3])