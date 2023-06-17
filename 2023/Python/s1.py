meters = 0

c = int(input())

column_1 = [int(i) for i in input().split()]
column_2 = [int(i) for i in input().split()]

last_vertical_adjacent_index = -1
attached = True

for i, entry in enumerate(column_1):
    if entry == 0:
        continue

    if i > 0 and entry == column_1[i-1]:
        meters += 1
        # print(f"c1 attached from top: {i}")
    else:
        if last_vertical_adjacent_index < 0:
            meters += 3
            attached = True
            # print(f"c1 isolated: {i}")

            if entry == column_2[i]:
                last_vertical_adjacent_index = i
                # print(f"last vertical {last_vertical_adjacent_index}")
            continue

        for j in range(i + 1 - last_vertical_adjacent_index):
            if column_2[j+last_vertical_adjacent_index] == 0:
                attached = False
        
        if attached:
            meters += 1
            # print(f"c1 attached from bottom: {i}")
        else:
            meters += 3
            attached = True
            # print(f"c1 isolated: {i}")
    
    if entry == column_2[i]:
        last_vertical_adjacent_index = i
        # print(f"last vertical {last_vertical_adjacent_index}")
            

attached = False
for i, entry in enumerate(column_2):
    if entry == 0:
        continue
    
    if ((i + 1) % 2 == 0) and (entry == column_1[i]):
        if (c < 2 or entry != column_2[i-1]) and (i >= c - 1 or entry != column_2[i+1]):
            meters += 3
            # print(f"even from bottom isolated: {i}")
            continue
        elif (c < 2 or entry != column_1[i-1]) and (i >= c - 1 or entry != column_1[i+1]):
            meters += 3
            # print(f"even from top isolated: {i}")
            continue

    if (i > 0 and entry == column_2[i-1]) or entry == column_1[i]:
        meters += 1
        # print(f"c2 attached: {i}")
    else:
        attached = False
        for j in range(c - i):
            if column_2[i+j] == 0:
                break

            if column_1[i+j] == 1:
                attached = True

        if attached:
            meters += 1
            # print(f"c2 attached from top: {i}")
        else:
            meters += 3
            # print(f"c2 isolated: {i}")

print(meters)