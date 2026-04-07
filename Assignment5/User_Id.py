correct_Userid = "nisha"
correct_Pass = "abc123"

attempts = 3

while attempts > 0:
    userid = input("Enter UserID :")
    password = input("Enter Password :")

    if userid == correct_Userid and password == correct_Pass:
        print("Login successful !! Welcome.")
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect credentials.You have {attempts} attempts left.")
        else:
            print(f"Incorrect credentials.No attempts left.")