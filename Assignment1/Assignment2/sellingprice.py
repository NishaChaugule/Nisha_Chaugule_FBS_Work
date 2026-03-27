cost_price = int(input('Enter cost price:'))
discount_percent = int(input('Enter discount percent:'))

discount_amount = cost_price * (discount_percent/100)

selling_price = cost_price - discount_amount

print('Discount amount of the book is:',discount_amount)
print('selling price of the book is:',selling_price)