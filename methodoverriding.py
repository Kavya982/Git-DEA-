class BusBookApp:
    def facilities(self):
        print("we can provide bed sheet along with pillow")
class RedBus(BusBookApp):
    def facilities(self):
        super().facilities()
        print("we can also provide water bottles and amazing discounts")

r = RedBus()
# b=BusBookApp()
# b.facilities()
r.facilities()