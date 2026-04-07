num = int(input("Enter number :"))
a = 0
b = 1
print("Fabonacci series :")
for i in range (num):
    print(a , end=" ")
    c = a + b
    a = b
    b = c
