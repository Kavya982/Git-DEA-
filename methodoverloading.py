#python doesnot supports method overloading directly but it supports indirectly with the help of default argumnets
class Addition:
    def add(self,a=None,b=None,c=None,d=None):
        if(a!=None and b!=None and c!=None and d!=None):
            print("sum is ",a+b+c+d)
        elif(a!=None and b!=None and c!=None):
            print("sum is ",a+b+c)
        elif(a!=None and b!=None):
            print("sum is ",a+b)
        else:
            print("sum is ",a)
a = Addition()
a.add(2,3,4,5)
a.add(1)
a.add(2,5)
a.add(1,8,6)


class Subtraction:
    def sub(self,*arg):
        res=0
        for i in arg:
            res=i-res
        print("subtraction for the provided numbers ",res)

s= Subtraction()
s.sub(1,2,3,4)
s.sub(10,3)



        