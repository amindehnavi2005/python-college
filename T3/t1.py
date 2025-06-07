number1 = int(input("enter number 1:"))
number2 = int(input("enter number 2:"))
number3 = int(input("enter number 3:"))

def biggest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
print(biggest(number1,number2,number3))