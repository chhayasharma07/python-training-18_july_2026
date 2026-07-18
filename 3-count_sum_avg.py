dbms=int(input("Enter the marks of DBMS : "))
python=int(input("Enter the marks of python : "))
dsa=int(input("Enter the marks of dsa : "))
maths=int(input("Enter the marks of maths : "))
oops=int(input("Enter the marks of oops : "))

sum=dbms+python+dsa+maths+oops
length=len([dbms,python,dsa,maths,oops])
avg=sum/length

print(f"The sum of all marks is : {sum}")
print(f"The avg of all marks is : {avg}")
print(f"The count of all subjects is : {length}")
