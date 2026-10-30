#For Loop
for i in range(5):
    print(i)

#While Loop
i=1
while i<=5:
    print(i)
    i=i+1

#Break
for i in range(10):
    if i==5:
        break
        print(i)

#Contiue
for i in range(6):
    if i==3:
        continue
    print(i)

#Pass
for i in range(5):
    print(i)
else:
    print("Loop Completed")

#Factorial using For Loop
    
num=int(input("Enter Number : "))
fact=1
for i in range(1,num+1):

    fact=fact*i

print("Factorial =",fact)

#Factorial using While Loop

num=int(input("Enter Number : "))
fact=1
i=1
while i<=num:
    fact=fact*i
    i=i+1
print("Factorial =",fact)

#Demonstration of break

for i in range(1,11):
    if i==6:
        break
    print(i)

#Demonstration of continue

for i in range(1,11):
    if i==6:
        continue
    print(i)

#Demonstration of pass

for i in range(5):
    pass
print("Loop Finished")

#Demonstration of else with loop

for i in range(1,6):
    print(i)
else:
    print("Loop Executed Successfully")

#Fibonacci Series

a=0
b=1
print(a,b,end=" ")
for i in range(2,n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c

#Prime Number

num=int(input("Enter Number : "))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("Prime")
else:
    print("Not Prime")
    
#Armstrong Number

num=int(input("Enter Number : "))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if sum==num:
    print("Armstrong")
else:
    print("Not Armstrong")

#Number Palindrome

num=int(input("Enter Number : "))
temp=num
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if rev==num:
    print("Palindrome")
else:
    print("Not Palindrome")

#Multiplication Table

n=int(input("Enter Number : "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)

 





