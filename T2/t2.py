countNumber =10
totalTrue =0

for i in range(countNumber):
    num =int(input(f"Enter Number {i+1} :"))
    if num %4 ==0 :
        totalTrue +=1
    
print(f"Count Number % 4 == 0 -> {totalTrue}")