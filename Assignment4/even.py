start=int(input("Enter the Starting no= "))
end=int(input("Enter the Ending no= "))
print(f"the Even no. from {start} to {end} are:= ")
for i in range(start,end):
    if i % 2 == 0:
        print(i)