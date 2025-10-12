rows, cols           = map(int, input().split())
start_row, start_col = map(int, input().split())
end_row, end_col     = map(int, input().split())

grid = [input() for _ in range(rows)]

off = (
  (-1, 0), # Up
  (0,  1), # Right
  (1,  0), # Down
  (0, -1), # Left
)

names = (
  "Up", "Right", "Down", "Left"
)

def add(a,b):
  return (a[0]+b[0],a[1]+b[1])

def query_cell(r,c=None):
  if type(r) == tuple:
    r,c = r
  if r < 0: return False
  if c < 0: return False
  if r > rows-1: return False
  if c > cols-1: return False
  if grid[r][c] != "0": return False
  return True

def left(d):
  return ((d - 1) % 4)

def right(d):
  return ((d + 1) % 4)

graph = {}
for r, row in enumerate(grid):
  for c, cell in enumerate(row):
    for d in range(4):
      # Try to turn left and go forward
      lf = add(off[left(d)], (r,c))
      f = add(off[d],(r,c))
      if query_cell(lf):
        graph[(r,c,d)] = (*lf, left(d))
      elif query_cell(f):
        graph[(r,c,d)] = (*f, d)
      else:
        graph[(r,c,d)] = (r,c,right(d))

visited = set()
cur = (start_row, start_col, 1)
while True:
  print(cur[0], cur[1], names[cur[2]])
  if cur in visited:
    print("0")
    break
  visited.add(cur)
  if cur[0] == end_row and cur[1] == end_col:
    print("1")
    break
  if cur in graph:
    cur = graph[cur]
  else:
    print("0")
    break