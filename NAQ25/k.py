def is_chest(inp):
  print("? " + inp)
  return input() == "1"

def ans(inp):
  print("! " + inp)
  exit()

if is_chest("3 2"):
  if is_chest("2 1"):
    ans("2 1")
  if is_chest("2 3"):
    ans("2 2")
  if is_chest("4 1"):
    ans("3 1")
  if is_chest("4 3"):
    ans("3 2")
if is_chest("2 4"):
  if is_chest("1 3"):
    ans("1 3")
  if is_chest("3 3"):
    ans("2 3")
  if is_chest("1 5"):
    ans("1 4")
  ans("2 4")
if is_chest("4 4"):
  if is_chest("3 4"):
    if is_chest("3 3"):
      ans("3 3")
    ans("3 4")
  if is_chest("5 3"):
    ans("4 3")
  ans("4 4")
if is_chest("1 2"):
  if is_chest("2 1"):
    ans("1 1")
  ans("1 2")
if is_chest("5 1"):
  ans("4 1")
ans("4 2")