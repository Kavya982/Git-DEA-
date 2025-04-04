class Mobile:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def whatsApp(self):
        print("Thanks for using whats app") 
class Redmi(Mobile):
    def instagram(self):
        print("I am sure u r enjoying insta")
r1 = Redmi("Redmi note 8","gray")
r1.whatsApp()
r1.instagram()