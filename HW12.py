#Name: Eden Xie
#Class: 6th Hour
#Assignment: HW12


#1. Print Hello World!
print("This place was not for you to look, take it from me")
#2. Create three different boolean variables named wifi, login, and admin.
Wifi=True
Login=True
Admin=True
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
AdminLogin=0
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if Wifi==True:
    if Login==True:
       if Admin==True:
           print("Welcome")
           print(AdminLogin + 1)
       else:
           print("Missing Admin")
    else:
        print("Missing Login")
else:
    print("Missing Wifi")
