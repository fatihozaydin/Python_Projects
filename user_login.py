print("""********************
User Login:
********************
    """)

sys_user_name = ("fatih")
sys_password = "123456"

user_name = input("User_Name: ")
password = input("Password: ")


if (sys_user_name == user_name and sys_password != password):
    print("The Password Is Incorrect...")
elif (sys_user_name != user_name and sys_password == password):
    print("The Username Is Incorrect...")
elif (sys_user_name != user_name and sys_password != password):
    print("Username and Password is incorrect...")
else:
    print("System Login Successfully...")
