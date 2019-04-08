fileptr=open("file.txt","r")
a=fileptr.read()
print(a)
fileptr.close()

filesptr=open("file.txt","r")
print("file pointer is at byte :",filesptr.tell())
content=filesptr.read()
filesptr.seek(65)
print("after reading file pointer is at byte :",filesptr.tell())

import os;

os.rename("file.txt","FILE.txt")
if os.rename:
        print("ok")
else:
    print("not ok")


os.remove("FILE.txt")

temp=[10,-20,-289,100]
def c_to_f(c):
        if c<-273.15:
            print("does not exist")
        else:
            f=c*9/5+32
            return f
for t in temp:
    print(c_to_f(t))

    import subprocess



