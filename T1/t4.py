num = int(input("Enter a Number : "))
binary= 0
count = 0

while num != 0 :
    binary = binary + (num % 2) * (10 ** count)
    num=num // 2
    count+=1

print("binary number :{0:5d}".format(binary))