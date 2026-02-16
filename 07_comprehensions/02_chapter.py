# Set comprehension

chai_orders = [
    "Masala chai", "Green tea", "Lemon tea", "Masala chai", "Green tea", "Ginger chai"
]

unique_chai = {chai for chai in chai_orders}
print("Unique chai : ",unique_chai)

chai_recepies = {
    "Masala chai" : ["Ginger", "Clove", "Cardamom"],
    "Elaichi chai" : ["Cardamom" , "Milk"],
    "Spicy chai" : ["Ginger", "Black pepper", "Clove"]
}

unique_spices = {spice for ingredients in chai_recepies.values() for spice in ingredients}
print("Unique spices : ",unique_spices)