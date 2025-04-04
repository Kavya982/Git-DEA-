class BankAccount:

    def __init__(self,name,balance):
        self._name=name
        self.__balance=balance 

    def displayDetails(self):
        print(self._name," ",self.__balance) 

b = BankAccount("suma",340000)

b.displayDetails()

print(b._name)


        