num = int(input('Enter Number :'))
temp = num
d1 = temp % 10
temp = temp // 10

d2 = temp % 10
temp = temp // 10

d3 = temp % 10
temp //= 10

rev = d1*100 + d2*10 + d3

print('reversed number is:',rev)