#S1 2021: Crazy fencing

plank_num = int(input())
plank_areas = []
plank_widths = []
plank_heigts = []

heights = input().split(' ', plank_num + 1)
for i in range(plank_num + 1):
  plank_heigts.append(int(heights[i]))

widths = input().split(' ', plank_num)
for i in range(plank_num):
  plank_widths.append(int(widths[i]))

for i in range(plank_num):
  area = plank_widths[i] * ((plank_heigts[i] + plank_heigts[i+1]) / 2)
  plank_areas.append(area)

print(sum(plank_areas))