class Chai():

    def __init__(self, sweetness, milk_amount):
        self.sweetness = sweetness
        self.milk_amount = milk_amount

    def sip(self):
        print("Sipping tea")
    
    def add_sugar(self, amount):
        print("Added sugar")

myChai = Chai(sweetness=2, milk_amount=2)

myChai.sip()
myChai.add_sugar(3)