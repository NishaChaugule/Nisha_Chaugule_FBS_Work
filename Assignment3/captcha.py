import random

correct_id = "nisha"
correct_pass = "abc123"

entered_userid = input("Enter Userid :")
entered_pass = input("Enter Password :")

if(entered_userid == correct_id and entered_pass == correct_pass):
    print("Successful!!")

    captcha = random.randint(1000, 9999)
    print(captcha)

    user_input = input("Enter 4 digit captcha :")

    if (user_input == str(captcha)):
        print("Success!! Verification is complete!!")    
    else:
        print("Failed !! Incorrect code...")
else:
    print("Invalid User Id or Password")

 