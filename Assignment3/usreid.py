correct_id = "nisha"
correct_pass = "abc123"

entered_userid = input("Enter Userid :")
entered_pass = input("Enter Password :")

if(entered_userid == correct_id and entered_pass == correct_pass):
    print("Login Successful!!")

else:
    print("Invalid User Id and Password")