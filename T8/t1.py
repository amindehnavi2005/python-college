#* Open File Write Data
file = open("test.dat","w")
while True:
    student = input("Enter Student Name:")
    if student == "" :
        break
    file.write(student+"\n")
file.close()

#Open File Read Data
file = open("test.dat","r")
student = file.read()
while student != "" : 
    print(student)
    student = file.read()
file.close()