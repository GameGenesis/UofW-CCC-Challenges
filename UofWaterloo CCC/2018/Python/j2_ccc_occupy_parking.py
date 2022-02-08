#Problem J2: Occupy parking (2018 UofWaterloo CCC)

n = 0
parking_yesterday = ""
parking_today = ""
parking_occupied_twice = 0

def clamp(n, min_n, max_n):
    return max(min(n, max_n), min_n)

n = int(input())
n = clamp(n, 1, 100)

parking_yesterday = input()
parking_today = input()

for chr in range(n):
    try:
        if(parking_yesterday[chr] == "C" and parking_today[chr] == "C"):
            parking_occupied_twice += 1
    except:
        break

print(parking_occupied_twice)