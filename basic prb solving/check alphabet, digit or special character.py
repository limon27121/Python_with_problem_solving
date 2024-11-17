# A character is alphabet if it in between a-z or A-Z.
# A character is digit if it is in between 0-9.
# A character is special symbol character if it neither alphabet nor digit.

Input=input("Enter Your input:")

if 'a' <= Input <= 'z':
    print("Small letter")

elif(Input>='A' and Input<='z'):
    print("capital letter")

elif(Input>='0' and Input<='9'):
    print("{} is a digit".format(Input))


else:
    print("{} is special character".format(Input))



