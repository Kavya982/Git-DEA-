class Mother:
    def iq(self):
        print("usually kids IQ is inherited form their mother") 
    def color(self):
        print("color is either from mother")
class Father:
    def height(self):
        print("children height inherited from their father")
    def color(self):
        print("color is either from father") 
class Child(Father,Mother):
    def job(self):
        print("This is the only thing we donot meant to be inherited from parents. Fully our responsibility")
    

c = Child()
c.iq()
c.height()
c.job()
c.color()