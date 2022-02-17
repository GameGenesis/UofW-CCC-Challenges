#Works; not optimized

x = int(input())
same_groups_2 = []
violations = 0

for i in range(x):
    same_groups_2.append(input())

y = int(input())
different_groups_2 = []

for i in range(y):
    different_groups_2.append(input())

g = int(input())
groups = []

for i in range(g):
    groups.append(input().split())

length = max(x, y)
for i in range(length):
    done_1 = False
    done_2 = False
    for j in range(g):
        if i < x and not done_1:
            same_groups_split = same_groups_2[i].split()
            if same_groups_split[0] in groups[j] or same_groups_split[1] in groups[j]:
                if not(same_groups_split[0] in groups[j] and same_groups_split[1] in groups[j]):
                    violations += 1
                    #print("Same: ", same_groups_split, " in ", groups[j])
                    done_1 = True
        
        if i < y and not done_2:
            different_groups_split = different_groups_2[i].split()
            if different_groups_split[0] in groups[j] or different_groups_split[1] in groups[j]:
                if different_groups_split[0] in groups[j] and different_groups_split[1] in groups[j]:
                    violations += 1
                    #print("Diff: ", different_groups_split, " in ", groups[j])
                    done_2 = True
            
print(violations)