num1=int(input("Enter a number = "))
num2=int(input("Enter another number = "))
#Basic method
# print("Arithmetic operations that can be performed on these numbers are : ")
# print("Addition of {} , {} is {}".format(num1,num2,(num1+num2)))
# print("Subtraction of {} , {} is {}".format(num1,num2,(num1-num2)))
# print("Multilplication of {} , {} is {}".format(num1,num2,(num1*num2)))
# print("Division(Quoitenet) of {} , {} is {}".format(num1,num2,(num1//num2)))
# print("Modulo Division(Remainder) of {} , {} is {}".format(num1,num2,(num1%num2)))

#Using match-case similiar to switch-case in java
option = int(input("1.Addtion\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulo Division\nEnter option\n"))
match option:
    case 1:
        print("Addition of {} , {} is {}".format(num1,num2,(num1+num2)))
    case 2:
        print("Subtraction of {} , {} is {}".format(num1,num2,(num1-num2)))
    case 3:
        print("Multilplication of {} , {} is {}".format(num1,num2,(num1*num2)))
    case 4 :
        print("Division(Quoitenet) of {} , {} is {}".format(num1,num2,(num1//num2)))
    case 5 :
        print("Modulo Division(Remainder) of {} , {} is {}".format(num1,num2,(num1%num2)))
    case _:
        print("Enter valid option")



