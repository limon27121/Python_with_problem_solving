Number=float(input("enter your number: "))

if(Number>=80 and Number<=100):
    result='A+'
elif(Number>=70 and Number<=79):
    result='A'
elif(Number>=60 and Number<=69):
    result='A-'
elif(Number>=50 and Number<=59):
    result='B'
elif(Number>=40 and Number<=49):
    result='C'
elif(Number>=33 and Number<=39):
    result='D'
elif(Number>=0 and Number<=32):
    result='F'

else:
    result="invalid number"

print("Your Grade is:",result)

