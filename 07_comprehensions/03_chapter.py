# Dictionary comprehensions

price_in_inr = {
    "Masala chai" : 40,
    "Green tea" : 50,
    "Lemon tea" : 200
}

price_in_usd = {chai:price/80 for chai, price in price_in_inr.items()}
print("Prices in usd : ",price_in_usd)