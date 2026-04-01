cp = int(input("enter cost price :"))
sp = int(input("enter selling price :"))

if (sp > cp ):
    profit = sp - cp
    print(f"profit of : {profit}")
elif(cp > sp):
    loss = cp - sp
    print(f"loss is : {loss}")
else:
    print("no profit,no loss")