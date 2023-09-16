# a="hello,world"

# print(a[1])

# for i in a:
#     print(i)

# print(len(a))

# if("world" in  a):
#     print("found")
  
# str1="hi"
# str2="limon"  
# str3=str1+" "+str2

# print(str3)

# print(str2[1:5])

# a="hello"
# a=a+"v"
# print(a)


import datetime
birthyear=int(input("enter your year: "))
x = datetime.datetime.now()

year=x.year-birthyear

print("your age is:{}".format(year))
