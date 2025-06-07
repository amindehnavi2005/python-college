# open file for write data
f = open("test1.dat", "w")
while True :
   st = input("Enter a course title : ")
   if st == "" :
       break
   f.write(st + "\n")
f.close()

# open file for read data
f = open("test1.dat", "r")
print("Contents of file using readline() : ")
s = f.readline()
while s != "" :
   print(s, end = "")
   s = f.readline()
f.close()
print("Contents of file using in operator : ")
f = open("test1.dat", "r")
for s in f:
    print(s, end = "")