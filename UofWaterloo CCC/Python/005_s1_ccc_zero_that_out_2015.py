#Problem S1: Zero That Out (2015 UofWaterloo CCC)

num_of_ints = 0
ints = []
sum_of_ints = 0

def clamp(n, min_n, max_n):
  return max(min(n, max_n), min_n)

num_of_ints = int(input())
num_of_ints = clamp(num_of_ints, 1, 100000)

for i in range(num_of_ints):
  current_int = int(input())
  current_int = clamp(current_int, 0, 100)

  if current_int == 0:
    ints.pop(len(ints) - 1)
  else:
    ints.append(current_int)

for i in ints:
  sum_of_ints += i

print(sum_of_ints)