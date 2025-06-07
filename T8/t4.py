import pickle
import os
class student:
    def __init__ (self, name, stno, ave):
        self.name = name
        self.stno = stno
        self.ave = ave
    #------------------------------
    def display(self):
       print("{0:10s} {1:5d} {2:8.2f}".format(self.name, self.stno, self.ave))
## Functions  ##
def menu():
    print("1. Enter a student ")
    print("2. Search a student ")
    print("3. Delete a student ")
    print("4. Update the ave of student ")
    print("5. Display all students")
    print("6. Exit ")
    choice = int(input("Enter your selection(1-6) : "))
    return choice
#--------------------------------------------
def insertData():
    print("Enter name, stno, ave :", end = "")
    name, stno, ave = input().split() 
    ob = student(name, int(stno), float(ave))
    pickle.dump(ob, myfile)
#------------------------------------
def reportData():
    myfile.seek(0, 0)
    ob = pickle.load(myfile)
    print("{0:10s} {1:10s} {2:10s}".format("Name", "Stno", "Ave"))
    while True:
        ob.display()
        try:
            ob = pickle.load(myfile)
        except(EOFError) as err:
            break
#---------------------
def searchData():
    myfile.seek(0, 0)
    stno = int(input("Enter a stno to search : "))
    found = False
    ob = pickle.load(myfile)
    while True:
       if ob.stno == stno :
           found = True
           break
       try :
          ob = pickle.load(myfile)
       except(EOFError) as err :
          break
    if found :
       print("{0:10s} {1:10s} {2:10s}".format("Name", "Stno", "Ave"))
       ob.display()
    else :
       print("Student not found : ")
#---------------------------
def updateData():
    outfile = open("stfile1.dat", "wb")
    print("Enter stno and ave to change ", end = "")
    stno , ave = input().split()
    myfile.seek(0, 0) 
    ob = pickle.load(myfile)
    found = False
    while True :
        if ob.stno == int(stno) :
            found = True
            ob.ave = float(ave)
            pickle.dump(ob, outfile)
            break
        else :
            pickle.dump(ob, outfile)
            try :
                ob = pickle.load(myfile)
            except(EOFError) as err :
                 break
    ## end of while -------------------
    if found : ## read the rest records and append to new file
        while True :
            try :
                 ob = pickle.load(myfile)
                 pickle.dump(ob, outfile)
            except(EOFError) as err :
                 break
       ## end of while
    ## end of if found
    myfile.close()
    outfile.close()
    os.remove("stfile.dat")
    os.rename("stfile1.dat", "stfile.dat")
#----------------------------------------
def deleteData():
    outfile = open("stfile1.dat", "wb")
    stno = int(input("Enter stno to delete :"))
    myfile.seek(0, 0)
    ob = pickle.load(myfile)
    found = False
    while True :
        if ob.stno == int(stno) :
            found = True
            break
        else :
            pickle.dump(ob, outfile)
            try :
                ob = pickle.load(myfile) 
            except(EOFError) as err :
                 break
    ## end of while ----------------------------
    if found : ## read the rest records and append to new file
        while True :
            try :
                 ob = pickle.load(myfile)                
                 pickle.dump(ob, outfile)
            except(EOFError) as err :
                 break
       ## end of while
    ## end of if found
    myfile.close()
    outfile.close()
    os.remove("stfile.dat")
    os.rename("stfile1.dat", "stfile.dat")
##  Driver program ---------
myfile = open("stfile.dat", "a+b") 
while True:
    c = menu()
    if c == 1:
        insertData()
    elif c == 2:
        searchData()
    elif c == 3:
        deleteData()
        myfile = open("stfile.dat", "a+b")                           
    elif c == 4:
        updateData()
        myfile = open("stfile.dat", "a+b") 
    elif c == 5:
        reportData()
    else:
        break