rframes = []
yframes = []
for _ in range(10):
  line1 = list(map(int, input().split()))
  r = []
  for i in range(1, line1[0]+1, 2):
    r.append((line1[i], line1[i+1]))
  line2 = list(map(int, input().split()))
  y = []
  for i in range(1, line2[0]+1, 2):
    y.append((line2[i], line2[i+1]))
  rframes.append(r)
  yframes.append(y) 


from math import sqrt
def dist(x, y):
  return sqrt((x-144)**2 + (y-84)**2)

rscore = 0
yscore = 0


for i, j in zip(rframes, yframes):
  rdists = [dist(m, n) for m,n in i]
  rdists.sort()
  ydists = [dist(m, n) for m,n in j]
  ydists.sort()
  mr = min(rdists)
  my = min(ydists)
  if mr < my:
    for x in rdists:
      if x < my:
        rscore += 1
  else:
    for x in ydists:
      if x < mr:
        yscore += 1
  
print(rscore, yscore)