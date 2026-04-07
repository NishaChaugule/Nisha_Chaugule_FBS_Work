n = int(input("Enter number :"))
i = 1
print("Numbers are not divisible by 2,3")
for i in range(i,n+1):
        if(i % 2!=0 and i % 3 != 0):
            print(i)
            i = i + 1