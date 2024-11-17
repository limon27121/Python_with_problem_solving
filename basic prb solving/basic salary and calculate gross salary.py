salary=float(input("enter your salary:"))
if(salary<0):
   print("invalid salary")
    
elif(salary<=10000):
    HRA=salary*(20/100)
    DA=salary*(80/100)
    total_salary=salary+HRA+DA
    print("your salary is: ",total_salary)

elif(salary>=10001 and salary<=20000):
    HRA=salary*(25/100)
    DA=salary*(90/100)
    total_salary=salary+HRA+DA
    print("your salary is: ",total_salary)

elif(salary>=20001):
    HRA=salary*(0.30)
    DA=salary*(0.95)
    total_salary=salary+HRA+DA
    print("your salary is: ",total_salary)
  

else:
    print("invalid input")

