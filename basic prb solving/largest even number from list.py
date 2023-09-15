def even(li):
    even=0
    max=li[0]
    for i in li:
        if(i%2==0):
            even=i
        if(even>max):
            max=even
         
    print(max) 

even([1,2,4,10,11])