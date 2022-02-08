#S2 2014: Assigning Partners

number_of_students = int(input())

member_names_1 = input().split(" ")
member_names_2 = input().split(" ")
members = []

match = True

for i in range(number_of_students):
    if len(members) == 0:
        members.append([member_names_1[i], member_names_2[i]])

    for j in range(len(members)):
        if member_names_1[i] in members[j] or member_names_2[i] in members[j]:
            if member_names_1[i] == member_names_2[i]:
                match = False
                break
            
            if member_names_1[i] in members[j] and member_names_2[i] in members[j]:
                break
            else:
                match = False
                break
        else:
            members.append([member_names_1[i], member_names_2[i]])
if match:
    print("good")
else:
    print("bad")