n = int(input("Enter number of student :"))
total_per = 0
for i in range(n):
    print("student", i+1)
    total = 0
    for j in range(5):
        marks = int(input("Enter marks: "))
        total += marks

    per = total / 5
    print("Percentage =",per)

    total_per += per

avg = total_per / n
print("Average Percentage of class =",avg)