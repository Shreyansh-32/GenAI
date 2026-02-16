# Generator basics

sales = [10, 9, 7, 5, 2, 12, 25, 19, 10, 7, 3, 5, 8]

total_cups = sum(cups for cups in sales if cups >= 2)
print("Total cups : ",total_cups)