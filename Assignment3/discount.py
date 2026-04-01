total_amout = 0
for i in range(1,6):
    print(f"Passanger {i}")
    age = int(input("Enter age :"))
    tic_price = float(input("Enter per person amount :"))

    if(age < 12):
        payable = tic_price * 0.70
        print(f"Chile discount applied...Payable = {payable}")

    elif(age > 59):
        payable = tic_price * 0.50
        print(f"Senior citizen Dicount applied...Payable = {payable}")

    else:
        payable = tic_price
        print(f"No discont...Payable = {payable}")

total_amout += payable

print(f"total ticket amount for all five passangers: {total_amout}")
