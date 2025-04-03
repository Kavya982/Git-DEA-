num = int(input("Enetr a number = "))
def fibonacci(num):
    a=0
    b=1
    if(num==1):
        print(a)
    elif(num==2):
        print(a,b)
    else:
        print(a,b)
        for i in range(3,num+1):
            c=a+b
            print(c)
            a,b=b,c
fibonacci(num)