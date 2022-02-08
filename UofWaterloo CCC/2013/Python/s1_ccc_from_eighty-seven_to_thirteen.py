#S1 2013: From 1987 to 2013
year_str = input()
distinct_year = int(year_str)

for i in range(int(year_str) + 1, 1000000):
  sorted_year = list(map(int, str(i)))
  sorted_year.sort()
  distinct = True
  for j in range(len(sorted_year) - 1):
    if sorted_year[j] == sorted_year[j+1]:
      distinct = False
  if distinct == True:
    distinct_year = i
    break

print(distinct_year)