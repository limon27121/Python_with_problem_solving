user_range=int(input("enter your range:"))
even_sum=0
odd_sum=0
for i in range(1,user_range+1,1):
    if(i%2==0):
        even_sum+=i
    else:
        odd_sum+=i

print("even sum is: ",even_sum)
print("odd sum is:",odd_sum)