#S1 2020: Surmising a Sprinter's Speed

input_strs = []
time_speeds = []
max_speed = -1000000000

n = int(input())

for i in range(n):
  input_strs.append(input())
  temp_list = [int(input_strs[i].split(" ")[0]), int(input_strs[i].split(" ")[1])]
  time_speeds.append(temp_list)

time_speeds.sort(reverse=True)

for i in range(len(time_speeds) - 1):
  delta_time = abs(time_speeds[i][0] - time_speeds[i+1][0])
  delta_distance = abs(time_speeds[i][1] - time_speeds[i+1][1])
  speed = delta_distance / delta_time
  
  if speed > max_speed:
    max_speed = speed

print(max_speed)