def chai_type(type = "Ginger"):
    """Returns the chai type with default value as ginger"""
    return type

print(chai_type.__doc__)
print(chai_type.__name__)

def bill_generator(chai = 0, samosa = 0):
    """"
    Calculate the total bill for chai and samosa

    :param chai: Number of chai cups(10 Rs. each)
    :param samosa: Number of samosa(15 Rs. each)

    :return: Total amount and thank you message as string
    """
    total = chai * 10 + samosa * 15
    return total, "Thank you! for visiting our store"