# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill.


unit=float(input("enter consume unit:"))

if(unit<=50):
    amount=unit*0.50

elif(unit<=150):
    amount=50*0.50+(unit-50)*0.75

elif(unit<=250):
    amount=50*0.50+100*0.75+(unit-150)*1.20

elif(unit>250):
    amount=50*0.50+100*0.50+100*1.20+(unit-250)*1.50

else:
    print("invalid input")

total_bill=amount+(amount*0.20);
print("total bill is:",total_bill,"taka")