#S1/J4 2019: Flipper
grid = [[1,2], [3,4]]

flips_str = input()
flips = list(flips_str)
v_flip_count = 0
h_flip_count = 0

for c in flips:
  if c == "V":
    v_flip_count += 1
  elif c == "H":
    h_flip_count += 1

if v_flip_count % 2 == 1:
  grid[0] = grid[0][::-1]
  grid[1] = grid[1][::-1]

if h_flip_count % 2 == 1:
  grid = grid[::-1]

print(f"{grid[0][0]} {grid[0][1]}")
print(f"{grid[1][0]} {grid[1][1]}")