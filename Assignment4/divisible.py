start = int(input("Enter start number :"))
end = int(input("Enter end number :"))
num = int(input("Enter number :"))

print(f"Numbers are divisible by {num} in range between {start} and {end} :")
for i in range(start,end+1):
        if(i % num == 0):
            print(i)
            