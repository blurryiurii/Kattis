n = input()
nums = list(map(int, input().split()))
a = nums[0] // 3
c = nums[-1] // 3
b = nums[1] - 2 * a
print(a,b,c)