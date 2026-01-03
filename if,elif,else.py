'''#if , elif ,else statement:
age =int(input("Enter the age:"))
if age>=18:
    print("he/she is an adult")
elif age<18:
    print("he/she is not an adult")



#pass fail using above statement
marks=int(input("Enter the marks:"))
if marks <= -1:
    print("absent")
elif marks>=35:
    print("pass")
else:
    marks<35
    print("fail")


#even or odd number
n=int(input("enter a Number: "))
if n%2==0:
    print("It is an Even Number")
elif n%2!=0:
    print("it is a odd number")'''
    
    
    
    
#loop mini task
n=int(input())
if n>0:
    print("positive Number")
elif n<0:
    print("negative Number")
else:
    n==0
    print("Zero")
for i in range (1,n+1):
    print(i)

