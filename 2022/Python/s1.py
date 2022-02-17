import math

n = int(input())
output = max(0, (n + 1) // 4 - math.ceil(n / 5)) + 1
print(output)