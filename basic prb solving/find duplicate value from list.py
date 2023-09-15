my_list=["a","b","b","c","c","d","e"]
'''
find duplicate value from list
'''

duplicate_list=[]

for i in my_list:
    if my_list.count(i)>1:
        if i not in duplicate_list:
            duplicate_list.append(i)

print(duplicate_list)