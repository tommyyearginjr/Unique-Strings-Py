list1 = ['a','b','c','a','d']

print(list1)
# >> ['a', 'b', 'c', 'a', 'd']

paredList1 = []

for i in list1:
    if i not in paredList1:
        paredList1.append(i)

print(paredList1)
# >> ['a', 'b', 'c', 'd']
