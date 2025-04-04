class Car:
    def __init__(self,name,model):
        self.name=name
        self.model=model 
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stoped")
class Ford(Car):
    def playmusic(self):
        print("music starts playing") 
class Suzuki(Ford):
    def playvideo(self):
        print("Video option also available here")

s1 = Suzuki("suzuki s9","white")
s1.start()
s1.stop()
s1.playmusic()
s1.playvideo()