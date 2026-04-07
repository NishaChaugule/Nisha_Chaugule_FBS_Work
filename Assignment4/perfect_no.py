num = int(input("Enter a number :"))
divisors_sum = 0

for i in range(1 , (num // 2) + 1):
    if num % i == 0:
        divisors_sum += i

if divisors_sum == num and num > 0:
    print(f"{num} is Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")