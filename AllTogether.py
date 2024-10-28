### Part Four -- your code goes here. 
import random
numbers = [random.randint(1, 100) for _ in range(10)]
print("Original list of numbers:", numbers)
check = 0
while check < len(numbers):
    if numbers[check] % 2 == 0:
        numbers.pop(check)
    else:
        check += 1
print("Remaining odd numbers:", numbers)