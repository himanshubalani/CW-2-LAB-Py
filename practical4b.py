#Aim: Implement Stacks using Lists
# create a stack names as Stackedlist. Insert Element 25, 20, 10, 5. POp 25,20 insert 15
#insert 20 , 25 . print stack. Pop  all elements.Insert elemnt 50 . print list
stackedlist = list()
stackedlist.append(25)
stackedlist.append(20)
stackedlist.append(10)
stackedlist.append(5)
stackedlist.remove(25)
stackedlist.remove(20)
stackedlist.append(15)
stackedlist.append(20)
stackedlist.append(25)
print(stackedlist)
stackedlist.clear()
stackedlist.append(50)
print(stackedlist)
