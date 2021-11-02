#S1 2018: Voronoi Villages

villages = []

def clamp(n, min_n, max_n):
  return max(min(n, max_n), min_n)

number_of_villages = int(input())
number_of_villages = clamp(number_of_villages, 3, 100)

for n in range(number_of_villages):
  villages.append(int(input()))

villages.sort()

smallest_size = 1000000000

for n in range(number_of_villages):
  if n > 0 and n < number_of_villages - 1:
    size_left = villages[n] - villages[n-1]
    size_right = villages[n+1] - villages[n]
    size = (size_left + size_right) / 2
    smallest_size = min(size, smallest_size)

print(smallest_size)