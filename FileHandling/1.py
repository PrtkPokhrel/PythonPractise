# 'r'=reading,'w'= writing,'a'=append
# f=open('FileHandling/file.py','r')
# rd=f.read()
# print(rd)
# f.close()

"""f=open('FileHandling/file.py','r')
rd=f.read()
print(rd)
f.close()
"""



# f=open('helloworld.c','w')  Creates a file name helloworld.c


# The following program write, appends and reads the file from file.txt

"""f=open('FileHandling/file.txt','w')
wd=f.write('Hello once again')
f.close()

g=open('FileHandling/file.txt','a')
ab=g.write(" from this computer: ")
g.close()

h=open('FileHandling/file.txt','r')
cd=h.read()
print(cd)
"""
# The following program takes the user input sums it and store in file.txt
num1=int(input("Enter the number: "))
num2=int(input("Enter another number: "))
value=num1+num2
print(value)

with open('FileHandling/file.txt','w') as f:
 store=f.write(str(num1)+'\n')
 store2=f.write(str(num2)+'\n')
 result=f.write(str(value)+'\n')
 



