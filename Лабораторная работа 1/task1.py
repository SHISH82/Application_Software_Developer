numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_none = numbers.index(None)

total_sum = 0
for i, num in enumerate(numbers):
 if i != index_none:
  total_sum += num

average = total_sum / len(numbers)

numbers[index_none] = average

print("Измененный список:", numbers)






