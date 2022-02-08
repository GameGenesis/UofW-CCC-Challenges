#Problem J4: Favourite Times  (2017 UofWaterloo CCC)

import math

duration = 0 #The input duration
clock_time_hour = 12 #The hour of the current time
clock_time_min = 0 #The minutes of the current time

#Current time in minutes
clock_time_total_min = (clock_time_hour * 60) + clock_time_min
#Clock sequence string
clock_sequence = ""
#Number of sequences present in the duration specified
arithmetic_sequences = 0

def clamp(n, min_n, max_n):
  return max(min(n, max_n), min_n)

#Clamped duration input
duration = int(input())
duration = clamp(duration, 0, 1000000000)

#array of differences between each digit
difference_between_digits = []

#Looping over each specified minute between the start time and the end time
for time in range(duration):
  #Increasing current time by one minute and calculating the current hour and minute
  clock_time_total_min += 1
  clock_time_hour = math.floor(clock_time_total_min / 60)
  if(clock_time_hour >= 13):
    clock_time_hour -= 12
  clock_time_min = clock_time_total_min % 60
  #String formatting - hmm or hhmm
  clock_sequence = f"{clock_time_hour}{clock_time_min:02d}"
  #print(clock_sequence)
  
  #Finding the differences between digits of each time
  x = 0
  last_digit = 0
  for digit in clock_sequence:
    if(x != 0):
      difference_between_digits.append(int(digit) - last_digit)
    last_digit = int(digit)
    x += 1

  first_element = difference_between_digits[0]
  #print(difference_between_digits)
  
  #Checking if digit differences array's elements are equal - digits are sequential
  sequential = True
  for d in difference_between_digits:
    if(d != first_element):
      sequential = False
  difference_between_digits.clear()
  
  #Increasing the arithmetic sequences counter & reseting the bool
  if(sequential):
    arithmetic_sequences += 1
    sequential = False

#Print Output
print(arithmetic_sequences)