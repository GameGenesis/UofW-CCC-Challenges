#WIP

import itertools

input_list = input().split()
number_of_notes, max_pitch_value, k  = int(input_list[0]), int(input_list[1]), int(input_list[2])
music = []
output = -1
good_samples = 0

pitch_list = []
for i in range(1, max_pitch_value + 1):
    pitch_list.append(i)

for i in range(1, number_of_notes + 1):
    pitch_list = list(itertools.permutations(pitch_list, i))
    for l in pitch_list:
        pass
    print(pitch_list)