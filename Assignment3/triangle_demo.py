side1 = float(input("Enter length of first side :"))
side2 = float(input("Enter length of second side :"))
side3 = float(input("Enter length of third side :"))

if(side1 == side2 == side3):
    print("Equilateral triangle")
elif(side1 == side2 or side2 == side3 or side1 == side3):
    print("Isosceles triangle")
else:
    print("Scalene triangle")
