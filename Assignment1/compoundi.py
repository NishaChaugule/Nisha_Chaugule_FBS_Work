Principle = int(input('Enter value of principle :'))
Rate = int(input('Enter value of rate :'))
Time = int(input('Enter value of time :'))

Compound_Interst = Principle * (1 + Rate/100)**Time - Principle

print('Compound interst is:',Compound_Interst)