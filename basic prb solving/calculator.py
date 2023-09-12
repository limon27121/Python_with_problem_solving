num1 = float(input("Enter your number: "))
num2 = float(input("Enter your number: "))
print("enter any of sign which you want \n sum(+) \n subtraction(-)\n multiplication(*) \ndivision(/)\n power(**)\n modulus(%) ")
char=input("enter your sign: ")

if(char=="+"):
    result=num1+num2

elif(char=="-"):
      result=num1-num2
elif(char=="*"):
    result=num1*num2 
elif(char=="/"):
     result=num1/num2
elif(char=="**"):
     result=num1**num2  
elif(char=="%"):
     result=num1%num2 
else:
    print("invalid output");
     
print("{}{}{}={}".format(num1,char,num2,result))
