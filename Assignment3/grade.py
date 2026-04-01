sub1 = int(input("Enter marks for subject 1 :"))
sub2 = int(input("Enter marks for subject 2 :"))
sub3 = int(input("Enter marks for subject 3 :"))
sub4 = int(input("Enter marks for subject 4 :"))
sub5 = int(input("Enter marks for subject 5 :"))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total /500) * 100
print(percentage)

if (percentage >= 75):
    print("Distinction")
elif(percentage >= 60):
    print("First class")
elif(percentage >=50):
    print("second class")
elif(percentage >= 35):
    print("pass")
else:
    print("Fail...")