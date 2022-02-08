#S1 2012: Don't pass me the ball!

import math

total_players = int(input()) - 1
player_sequence = 3
scoring_combinations = 0

if (total_players >= player_sequence):
  scoring_combinations = int(math.factorial(total_players) / (math.factorial(player_sequence) * math.factorial(total_players - player_sequence)))

print(scoring_combinations)