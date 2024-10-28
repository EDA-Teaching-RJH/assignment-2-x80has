### Part Three -- your code goes here. 
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numbers.sort()
numbers = [i for i in numbers if i!= 1]
numbers.extend([7, 8])
print(numbers)