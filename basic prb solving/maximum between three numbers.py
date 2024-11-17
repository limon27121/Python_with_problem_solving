number1=float(input("enter your first number:"))
number2=float(input("enter your second number:"))
number3=float(input("enter your third number:"))

if(number1>number2):
    if(number1>number3):
        print("maximum number is:",number1)
    else:
        print("maximum number is:",number3)

else:
    if(number2>number3):
        print("maximum number is:",number2)
    else:
        print("maximum number is:",number3)