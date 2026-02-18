class Chai:
    pass

class ChaiTime:
    pass

print(f"Type of class Chai is {type(Chai)}")

ginger_tea = Chai()

print(f"Type of ginger tea is : {type(ginger_tea)}")
print(f"Is ginger tea belong to type Chai : {type(ginger_tea) is Chai}")
print(f"Is ginger tea belong to type ChaiTime : {type(ginger_tea) is ChaiTime}")