# List Operations

numbers=[25,12,40,18]
print("Original List")
print(numbers)
numbers.append(50)
print("\nAfter Append")
print(numbers)
numbers.insert(2,100)
print("\nAfter Insert")
print(numbers)
numbers.remove(12)
print("\nAfter Remove")
print(numbers)
numbers.sort()
print("\nSorted List")
print(numbers)
numbers.reverse()
print("\nReverse Order")
print(numbers)

#List Slicing
numbers=[10,20,30,40,50,60]
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[::-1])

#Searching an Element
numbers=[25,12,18,45,60]
item=int(input("Enter Number : "))
if item in numbers:
    print("Found")
else:
    print("Not Found")

#Count Frequency
numbers=[10,20,30,10,40,20,10]
element=int(input("Enter Number : "))
print("Frequency =",numbers.count(element))

#Removing Duplicates
numbers=[10,20,30,10,40,20,10]
unique=list(set(numbers))
print(unique)

#Tuple Operations
languages=("Python","Java","C","R")
print(languages)
print(languages[1])
print(languages[1:3])
print(len(languages))

#Tuple Packing
student=101,"Rahul","MCA",8.7
print(student)

#Tuple Unpacking
student=(101,"Rahul",8.5)
roll,name,cgpa=student
print(roll)
print(name)
print(cgpa)

#Nested List
marks=[[75,80],[82,90],[91,88]]
print(marks)
print(marks[0])
print(marks[1][1])

#Matrix Addition
A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
C=[]
for i in range(2):
    row=[]
    for j in range(2):
        row.append(A[i][j]+B[i][j])
    C.append(row)
print(C)

#Largest Element in List
numbers=[12,45,67,22,90]
largest=max(numbers)
print("Largest =",largest)

#Smallest Element
numbers=[12,45,67,22,90]
print(min(numbers))

#Sum and Average
numbers=[25,30,45,20,10]
total=sum(numbers)
average=total/len(numbers)
print("Sum =",total)
print("Average =",average)
