num = int(input("Enter a number = "))
flag=True
for i in range(2,num//2+1):
    if(num%i==0):
        flag=False
        break 
print("Prime number") if(flag) else print("Not a prime number")