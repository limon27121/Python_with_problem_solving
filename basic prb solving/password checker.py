username=input("enter your user name:")
password=input("enter your password:")

length=len(password)
encript_pass="*" * length
print("your user name is {} and your password is:{}".format(username,encript_pass))