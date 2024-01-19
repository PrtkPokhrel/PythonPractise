import myModules as md
import datetime as dd

num1=int(input("Enter the number: "))
num2=int(input("Enter the second number: "))

result=md.sum(num1,num2)
print(result)

time=dd.datetime.now()
print(time)

x = dd.datetime.now()

print(x.year)
print(x.strftime("%A")) 