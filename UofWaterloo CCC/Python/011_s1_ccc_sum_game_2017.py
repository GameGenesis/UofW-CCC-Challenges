#S1 2017: Sum Game
days = int(input())
swifts = input().split(" ", days)
semaphores = input().split(" ", days)

swifts_runs = 0
semaphores_runs = 0

corresponding_days = []

for i in range(days):
  swifts_runs += int(swifts[i])
  semaphores_runs += int(semaphores[i])
  if swifts_runs == semaphores_runs:
    corresponding_days.append(i+1)

max_day = max(corresponding_days) if len(corresponding_days) > 0 else 0
print(max_day)