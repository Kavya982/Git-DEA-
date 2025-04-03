name=None
age=None
address=None 
mobilenumber=None
def getDetails():
    global name,age,address,mobilenumber
    name=input("Enter your name = ")
    age = int(input("Enter your age = "))
    address = input("Enter address = ")
    mobilenumber = input("Enter phone number = ")
   
def displayDetails():
    print("++++++++++++++++++++++++")
    print("Entered Details : \nName : ",name,"\nAge : ",age,"\nAddress : ",address,"\nMobile Number : ",mobilenumber)
    print("++++++++++++++++++++++++")
    

getDetails()
displayDetails()