no = 7
if (no > 1):
    
    for i in range(2, 7):
        if(no % 2 == 0):
            print(f"{no} is not prime.")
            # break
    else:
        print(f"{no} is prime")
else:
    print("number is not greater than 1.")