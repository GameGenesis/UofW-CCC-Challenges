#S1 2018: Voronoi Villages

village_positions = []
village_sizes = []

leftmost_village = 0
rightmost_village = 0

max_size = 1000000000
smallest_size = max_size

def clamp(n, min_n, max_n):
  return max(min(n, max_n), min_n)

number_of_villages = int(input())
number_of_villages = clamp(number_of_villages, 3, 100)

for n in range(number_of_villages):
  village_positions.append(int(input()))

village_positions.sort()
leftmost_village = village_positions[0]
rightmost_village = village_positions[-1]

for n in range(number_of_villages):
  if n > 0 and n < number_of_villages - 1:
    size_left = abs(village_positions[n] - village_positions[n-1]) / 2
    size_right = abs(village_positions[n+1] - village_positions[n]) / 2
    village_sizes.append(size_left + size_right)
  else:
    village_sizes.append(max_size)

for size in village_sizes:
  smallest_size = min(size, smallest_size)

print(smallest_size)