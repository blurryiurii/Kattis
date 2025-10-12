nums = input()

# just need the last number's "ones" digit
if nums[-1] == '0':
  print(10)
else:
  print(nums[-1])