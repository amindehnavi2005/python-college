import numpy as np

numbers = []

number = int(input(f"Enter number {len(numbers)+1} : "))

while number != 0:
    numbers.append(number)
    number = int(input(f"Enter number {len(numbers)+1} : "))
    
unique , counts = np.unique(numbers, return_counts=True)

print(unique, counts)

most_frequent = unique[np.argmax(counts)]

print(most_frequent)