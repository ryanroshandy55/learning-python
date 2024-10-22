# Join two lists
# The easiest way using operator +
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join using append. This will join all item from list22 into list1 one by one
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
    
print(list1)

# or we can use the extend() method, where the purpose to add elements from one list to another list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)