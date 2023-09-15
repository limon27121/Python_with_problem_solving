li=[1,2,3,4,5,6]
li1=["limon","deba","shovon"]

index=li1.index("limon")
print(index)
li1.insert(index,"arifin")
     
       
       
print(li1) 
print(li1)
print(li[-5:-2])
length=len(li)

for i in range(0,length):
    print(li[i])
    
li[1:3]=[100,200]

li.insert(3,300)
li.append(7)
li.extend(li1)

print(li)

li.reverse()
print(li)

li=[1,2,3,4,5,6]
print(li[-1::-1])


#store in new list
li=[1,2,3,4,5,6]
list1=sorted(li,reverse=True)
print(list1)
print(li)

#sort the main list
list1=[1,2,3,4,5,6]

list1.sort(reverse=True)
print(list1)

#list unpacking

list2=[100,200,300,400,500]
a,b,*others=list2
print(a)
print(b)
print(others)