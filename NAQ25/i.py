# import functools
# import itertools
# n = int(input())

# bonuses = [0]+list(map(int, input().split()))

# skill = list(map(int, input().split()))

# # try solo teams, then doubles, etc.
# # @functools.lru_cache()
# # def rolling_mean(*arr):

# def calc_avg_score(arr):
#   return sum(j/len(arr) for j in arr+[bonuses[len(arr)]])

# skill.reverse()

# # best = -float("inf")
# # for size in range(1,len(skill)+1):
# #   v = calc_avg_score(skill[-2:])

# # skill.sort()

# best = 0

# for i in range(1, n + 1):
#   # s = sum(skill[:i])
#   # s += bonuses[i - 1]
#   # avg = s / i
#   # avg = skill[:i]
#   avg = calc_avg_score(skill[:i])
#   best = max(best, avg)

# # # means = []

# # # n = 1
# # # avg = skill[0]
# # # means.append(avg + bonuses[0])
# # # for i in skill[1:]:
# # #   avg /= n
# # #   avg *= n - 1
# # #   avg += i / n
# # #   avg += bonuses[n-1] / n
# # #   means.append(avg)
# # #   avg -= bonuses[n-1] / n
# # #   n += 1


# print(best)

from itertools import combinations

n = int(input())

bonuses = list(map(int, input().split()))

abilities = list(map(int, input().split()))


best = 0

for i in range(1, n+1):
  for comb in combinations(abilities, i):
    avg = (sum(comb)+bonuses[i-1])/i
    best = max(best, avg)
  # avg = (sum(abilities[:i+1])+bonuses[i-1])/i
  # best = max(best, avg)

print(best)