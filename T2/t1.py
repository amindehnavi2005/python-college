countNums = int(input("Enter Count Numbers => "))
total = 0

for i in range(countNums):
    number = int(input(f"Enter {i+1} Number => "))
    total += number ** 3
    
print(f"Total Number => {total}")