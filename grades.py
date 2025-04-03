marks=int(input("Enter your grades = "))
print("Your grade is : ",end=" ")
if marks>=90 and marks<=100:
    print("A")
elif marks>=70 and marks<=80:
    print("B")
elif marks>=60 and marks<=70:
    print("C")
else:
    print("Failed")