asymmetric_values = ""
lowest_asymmetric_value = -1

number_of_mountains = int(input())

heights = [int(i) for i in input().split()]

for i in range(number_of_mountains):
    for j in range(number_of_mountains - i):
        starting_index = j
        ending_index = j + i + 1

        cropped_heights = heights[starting_index:ending_index]

        asymmetric_value = 0
        # print(cropped_heights)

        for k in range(round(len(cropped_heights) / 2)):
            asymmetric_value += abs(cropped_heights[k] - cropped_heights[-1-k])
            # print(f"{cropped_heights[k]} - {cropped_heights[-1-k]}")
        
        # print(f"{i}: asymmetric_value: {asymmetric_value}")
        if lowest_asymmetric_value < 0:
            lowest_asymmetric_value = asymmetric_value

        lowest_asymmetric_value = min(lowest_asymmetric_value, asymmetric_value)
        asymmetric_value = 0

    if asymmetric_values == "":
        asymmetric_values = str(lowest_asymmetric_value)
    else:
        asymmetric_values += f" {lowest_asymmetric_value}"
    lowest_asymmetric_value = -1

print(asymmetric_values)