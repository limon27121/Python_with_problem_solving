
##demo of delivery  system

area=input("enter your pick-up area: ")

if(area=="Mirpur"or area=="Farmgate" or area=="Dhanmondi"):
    total_price=float(input("enter your total amount: "))
    if(total_price>=600):
        print("shipping free")
    elif(300<=total_price<600):
        print("shipping cost 50tk")
    
    else:
        print("shipping cost 150tk")
 
        

elif(area=="Mohakhali" or area=="Gulshan"):
     total_price=float(input("enter your total amount: "))
     if(total_price>=800):
        print("shipping free")
     
          
     elif(500<=total_price<800):
        print("shipping cost 100tk")
    
     else:
        print("shipping cost 200tk")
       
   
       
else:
    print("shipping is not available right now")
        