r, g, b = map(int, input().split())
cr, cg, cb = map(int, input().split())
crg, cgb = map(int, input().split())


# IURII
r_desired = max(0, r - cr)
g_desired = max(0, g - cg)
b_desired = max(0, b - cb)

# print(r_desired, g_desired, b_desired)

crg -= r_desired
cgb -= b_desired

if g_desired > (crg + cgb) or crg < 0 or cgb < 0:
  print(-1)
else:
  print(r_desired + g_desired + b_desired)