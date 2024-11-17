number1=float(input("enter your first number:"))
number2=float(input("enter your second number:"))
print("enter your desire sign \n sum(+)\n subtract(-)\n multiplication(*)\n division(/)\n reminder(%)\n exponent(**)")

sign=input("enter your desired sign:")


if(sign=="+"):
    result=number1+number2
elif(sign=="-"):
    result=number1-number2
elif(sign=="*"):
    result=number1*number2
elif(sign=="/"):
    result=number1/number2
elif(sign=="%"):
    result=number1%number2
elif(sign=="**"):
    result=number1**number2

else:
   result="invalid sign"

print("My result is:",result)