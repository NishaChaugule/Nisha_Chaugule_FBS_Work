num = int(input("enter a number :"))

og_num = num

num_digits = len(str(num))
armstrong_sum = 0

temp = num
while temp > 0:
    digit = temp % 10    #to get lats digit
    armstrong_sum += digit ** num_digits  #raise digit to the power of total digits and add to sum
    temp //= 10    #removes the last digit

if og_num == armstrong_sum:
    print(f"{og_num} is an Armstrong number.")
else:
    print(f"{og_num} is not an Armstrong number.")

