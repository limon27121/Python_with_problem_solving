price=[10,30,500,200,50,200,100]
total_budget=1000;
count=0;

for i in price:
    total_budget-=i;
    if total_budget<0:
        break
    count+=1
    
print("buy the number of products is:",count)