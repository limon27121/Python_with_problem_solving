list1=list(range(0,11))

even_list=[i for i in list1 if i%2==0]
odd_list=[i for i in list1 if i%2!=0]

print(even_list)
print(odd_list)